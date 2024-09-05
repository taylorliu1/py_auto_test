import base64
from sys import prefix
from PowerStore.prime.swagger_client.configuration import Configuration
from PowerStore.prime.swagger_client.api_client import ApiClient
from PowerStore.prime.swagger_client.api.host_api import HostApi
from PowerStore.prime.swagger_client.api.volume_api import VolumeApi
from PowerStore.prime.swagger_client.models.volume_create import VolumeCreate
from PowerStore.prime.swagger_client.models.host_create import HostCreate
from PowerStore.prime.swagger_client.models.initiator_create_modify import InitiatorCreateModify
from PowerStore.prime.swagger_client.models.initiator_protocol_type_enum import InitiatorProtocolTypeEnum
from common.databases.database import database
from PowerStore.prime.swagger_client.models.app_type_enum import AppTypeEnum
from PowerStore.prime.swagger_client.models.volume_detach import VolumeDetach
from PowerStore.prime.swagger_client.models.volume_attach import VolumeAttach
from PowerStore.prime.swagger_client.rest import ApiException
from threading import Thread
from time import sleep
from PowerStore.prime.swagger_client.models.os_type_enum import OSTypeEnum
from utils.os.Esxi import EsxiExecutor
import json

from utils.restapi import APIRequest



class BlockImpl():

    def __init__(self):
        lst = database.get_data("select ip,user,password from pflex_objs;")
        self.ip = lst[0][0]
        self.user = lst[0][1]
        self.passwd = lst[0][2]
        self.restApi = APIRequest(self.ip,self.user,self.passwd)

    def get_sdc_id_by_ip(self,ip):
        result = self.restApi.run_pflex("POST","api/types/Sdc/instances/action/queryIdByKey",data={'ip':ip})
        return result
    
    def get_sdt_id_by_name(self,name):
        result = self.restApi.run_pflex('GET',"api/types/Sdc/instances")
        nvme_result = [host for host in  result if host["hostType"] == "NVMeHost"]
        for nvme_host in nvme_result:
            if nvme_host["name"] == name:
                return nvme_host["id"]
        return ""

    def create_vloume(self,number,hosts,ips,size,storagePool):       
        sdc_ids = []
        for ip in ips:
            sdc_id = self.get_sdc_id_by_ip(ip)
            sdc_ids.append(sdc_id)
        storagePoolId = ""
        storage_pools = self.restApi.run_pflex('GET',"api/types/StoragePool/instances")
        for storage_pool in storage_pools:
            if storage_pool['name'] == storagePool:
                storagePoolId = storage_pool['id']
        for i in range(number):
            # index = i % len(host_ids)
            name = "block_sdc"+"_"+database.generate_random_str(10)
            result = self.restApi.run_pflex("POST","api/types/Volume/instances",data={'name':name,'volumeSizeInGb':size,'storagePoolId':storagePoolId})
            if 'id' in result:
                index = 0
                for sdc_id in sdc_ids:
                    res = self.map_sdc_by_id(sdc_id,result['id'])
                    if not res:
                        print ("create volume {} successfully but failed map to host {}".format(name,hosts[index]) )
                        continue
                    print("create volume {} successfully and map to host {}".format(name,hosts[index]))
                    sql = "insert into sdc_volume_mapping (host, volume_name,volume_id,sdc_id) values ( '" + hosts[index] + "','" + name + "','" + result['id'] + "','"+sdc_id+"');"
                    database.insert_data(sql)
                    index += 1

    def create_vloume_nvme(self,number,hosts,names,size,storagePool):
        sdt_ids = []
        for name in names:
            sdt_id = self.get_sdt_id_by_name(name)
            sdt_ids.append(sdt_id)
        storagePoolId = ""
        storage_pools = self.restApi.run_pflex('GET',"api/types/StoragePool/instances")
        for storage_pool in storage_pools:
            if storage_pool['name'] == storagePool:
                storagePoolId = storage_pool['id']
        for i in range(number):
            # index = i % len(host_ids)
            name = "block_nvme"+"_"+database.generate_random_str(10)
            result = self.restApi.run_pflex("POST","api/types/Volume/instances",data={'name':name,'volumeSizeInGb':size,'storagePoolId':storagePoolId})
            if 'id' in result:
                index = 0
                for sdt_id in sdt_ids:
                    res = self.map_sdc_by_id(sdt_id,result['id'])
                    if not res:
                        print ("create volume {} successfully but failed map to host {}".format(name,hosts[index]) )
                        continue
                    print("create volume {} successfully and map to host {}".format(name,hosts[index]))
                    sql = "insert into sdc_volume_mapping (host, volume_name,volume_id,sdc_id) values ( '" + hosts[index] + "','" + name + "','" + result['id'] + "','"+sdc_id+"');"
                    database.insert_data(sql)
                    index += 1


    def map_sdc_by_id(self,sdc_id,volume_id):
        res = self.restApi.run_pflex("POST","api/instances/Volume::{}/action/addMappedSdc".format(volume_id),data={'sdcId':sdc_id,'allowMultipleMappings':'True','accessMode':'ReadWrite'})
        if len(res) > 0:
            print ("map sdc failue {}".format(res['message']))
            return False
        return True

    def get_volumes(self):
        volumes = self.restApi.run_pflex("GET","api/types/Volume/instances")
        out = []
        for v in volumes:
            out.append((v['id'],v['name'],v['type']))
        return out

    def remove_mapped_sdc_by_host(self,host):
        lst = database.get_data("select volume_id,sdc_id from sdc_volume_mapping where host='{0}';".format(host))
        for item in lst:
            volume_id = item[0]
            sdc_id = item[1]
            self.restApi.run_pflex("POST","api/instances/Volume::{}/action/removeMappedSdc".format(volume_id),data={'sdcId':sdc_id})
  

    def delete_volume(self):
        lst = database.get_data("select distinct volume_id from sdc_volume_mapping;")
        for item in lst:
            volume_id = item[0]
            self.restApi.run_pflex("POST","api/instances/Volume::{}/action/removeVolume".format(volume_id),data={'removeMode':'ONLY_ME'})