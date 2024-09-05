import base64
from concurrent.futures import ThreadPoolExecutor
import random
from PowerStore.prime.swagger_client.api.host_api import HostApi
from PowerStore.prime.swagger_client.api.volume_api import VolumeApi
from PowerStore.prime.swagger_client.models.app_type_enum import AppTypeEnum
from PowerStore.prime.swagger_client.models.volume_create import VolumeCreate
import json
from PowerStore.prime.swagger_client.configuration import Configuration
from PowerStore.prime.swagger_client.api_client import ApiClient
from common.databases.database import database
from PowerStore.prime.swagger_client.models.host_create import HostCreate
from PowerStore.prime.swagger_client.models.os_type_enum import OSTypeEnum
from PowerStore.prime.swagger_client.models.initiator_create_modify import InitiatorCreateModify
from PowerStore.prime.swagger_client.models.initiator_protocol_type_enum import InitiatorProtocolTypeEnum
from PowerStore.prime.swagger_client.models.volume_detach import VolumeDetach
from PowerStore.prime.swagger_client.models.volume_attach import VolumeAttach
from PowerStore.prime.swagger_client.rest import ApiException
from utils.os.Esxi import EsxiExecutor


class VolumeNVMeImpl():

    def get_trident_client(self):
        lst = database.get_data("select ip,user,password from trident_objs;")
        ip = lst[0][0]
        user = lst[0][1]
        passwd = lst[0][2]

        configuration = Configuration()
        configuration.host = "https://"+ip+"/api/rest"
        configuration.username = user
        configuration.password = passwd
        configuration.verify_ssl = False
        credentials = user + ':' + passwd
        token = base64.b64encode(credentials.encode())
        tclient = ApiClient(configuration=configuration, header_name="Authorization",
                            header_value='Basic ' + token.decode('utf-8'))
        return tclient
    
    def get_host_id_by_name(self,name):
        pst_client = self.get_trident_client()

        host_api = HostApi(pst_client)
        hosts = host_api.host_get()
        for host in hosts:
            if host.name == name:
                return host.id
            
        return ""

    def create_vloume(self,number,hosts,size):       
        pst_client = self.get_trident_client()
        host_ids = []
        for host in hosts:
            host_id = self.get_host_id_by_name(host)
            host_ids.append(host_id)
        volume_api = VolumeApi(pst_client)
        with ThreadPoolExecutor(max_workers=10) as executor:
            for i in range(number):
                # index = i % len(host_ids)
                executor.submit(self.async_create_volume,hosts, size, host_ids, volume_api)

    def async_create_volume(self, hosts, size, host_ids, volume_api):
        name = "nvme"+"_"+database.generate_random_str(10)
        volmue_create = VolumeCreate(name=name, size=size*1024*1024*1024,app_type=AppTypeEnum.OTHER)
        res = volume_api.volume_post(volmue_create)
        if res.id:
            volume = volume_api.volume_id_get(res.id)
            index = 0
            for host_id in host_ids:
                self.map_host_by_id(host_id,res.id)
                print("create volume {} successfully and map to host {}".format(name,hosts[index]))
                sql = "insert into host_volume_mapping (host, volume_name,volume_wwn, volume_id) values ( '" + hosts[index] + "','" + name + "','" + volume.wwn + "','" + res.id + "');"
                database.insert_data(sql)
                index += 1


    def create_nvme_host_by_name(self,vc,vc_user,vc_pass,host):
        pst_client = self.get_trident_client()
        esxiExecute = EsxiExecutor(vc,vc_user,vc_pass)
        host_api = HostApi(pst_client)
        host_nqn= esxiExecute.get_host_nqn_nvme(host)
        host_create = HostCreate(name=host,os_type=OSTypeEnum.ESXI,initiators = [InitiatorCreateModify(port_name=host_nqn,
        port_type=InitiatorProtocolTypeEnum.NVME)])
        res = host_api.host_post(host_create)
        if res.id:
            return True
        return False

    def get_volumes(self):
        pst_client = self.get_trident_client()
        volume_api = VolumeApi(pst_client)
        start = 0
        end = 1999
        increase = 2000
        out = []
        for i in range(100):
            start_point = start + increase*i
            end_point = end + increase*i
            ran = "{}-{}".format(start_point,end_point)
            try:
                volumes =volume_api.volume_get(ran=ran)
                out.extend(volumes)
            except ApiException as e:
                break
        return out

    def delete_host_by_name(self,host):
        pst_client = self.get_trident_client()
        host_api = HostApi(pst_client)
        host_id = self.get_host_id_by_name(host)
        if host_id:
            host_api.host_id_delete(host_id)

    def unmap_host_by_name(self,host):
        pst_client = self.get_trident_client()
        volume_api = VolumeApi(pst_client)
        host_id = self.get_host_id_by_name(host)
        lst = database.get_data("select volume_id from host_volume_mapping where host='{0}';".format(host))
        for item in lst:
            body = VolumeDetach(host_id=host_id)
            try:
                volume_api.volume_id_detach_post(item[0],body)
            except ApiException as e:
                js=json.loads(e.body)
                msg = js['messages'][0]['message_l10n']
                print(msg)
                continue
            

    def map_host_by_id(self,host_id,volume_id):
        pst_client = self.get_trident_client()
        volume_api = VolumeApi(pst_client)
        body = VolumeAttach(host_id=host_id)
        volume_api.volume_id_attach_post(volume_id,body)

    
    def delete_volume(self):
        lst = database.get_data("select distinct volume_id from host_volume_mapping;")
        pst_client = self.get_trident_client()
        volume_api = VolumeApi(pst_client)
        with ThreadPoolExecutor(max_workers=10) as executor:
            for item in lst:
                executor.submit(volume_api.volume_id_delete,item[0])


