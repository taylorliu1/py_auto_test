import base64
from collections import defaultdict
from sys import prefix
import requests
from PowerFlex.NAS.swagger_client.configuration import Configuration
from PowerFlex.NAS.swagger_client.api_client import ApiClient
from PowerFlex.NAS.swagger_client.api.nas_servers_api import NasServersApi
from common.databases.database import database
from PowerFlex.NAS.swagger_client.models.nas_servers_create import NasServersCreate
from PowerFlex.NAS.swagger_client.models.file_interface_create import FileInterfaceCreate
from PowerFlex.NAS.swagger_client import FileInterfacesApi
from PowerFlex.NAS.swagger_client.api.smb_shares_api import SmbSharesApi
from PowerFlex.NAS.swagger_client.models.smb_share_create import SmbShareCreate
from PowerFlex.NAS.swagger_client.api.smb_servers_api import SmbServersApi
from PowerFlex.NAS.swagger_client.models.smb_server_create import SmbServerCreate
from PowerFlex.NAS.swagger_client.api.nfs_servers_api import NfsServersApi
from PowerFlex.NAS.swagger_client.models.nfs_server_create import NfsServerCreate
from PowerFlex.NAS.swagger_client.models.nfs_export_create import NfsExportCreate
from PowerFlex.NAS.swagger_client.api.nfs_exports_api import NfsExportsApi
from PowerFlex.NAS.swagger_client.models.nfs_export_default_access_enum import NFSExportDefaultAccessEnum
from PowerFlex.NAS.swagger_client.api.file_systems_api import FileSystemsApi
from PowerFlex.NAS.swagger_client.models.file_system_create import FileSystemCreate
from PowerFlex.NAS.swagger_client.models.file_system_access_policy_enum import FileSystemAccessPolicyEnum
import paramiko
from threading import Thread
from time import sleep
from utils.kafka.kafkaProducerUtil import MessageProducer
from utils.os.Linux import Executor
from utils.restapi import APIRequest
import json


class ShareImpl():

    def __init__(self):
        lst = database.get_data("select ip,user,password from pflex_objs;")
        self.ip = lst[0][0]
        self.user = lst[0][1]
        self.passwd = lst[0][2]
        self.restApi = APIRequest(self.ip,self.user,self.passwd)

    @property
    def access_token_tokyo(self):
        url = 'https://{}/rest/auth/login'.format(self.ip)
        headers ={
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        data = {
            "username": self.user,
            "password": self.passwd
        }
        response = requests.post(url, json=data, headers=headers,verify=False).json()
        return response['access_token']

    def get_powerflex_client(self):
        configuration = Configuration()
        configuration.host = "https://"+self.ip+"/rest/v1"
        configuration.verify_ssl = False

        pflex = ApiClient(configuration=configuration, header_name="Authorization",
                            header_value='Bearer ' + self.access_token_tokyo)
        return pflex

    def get_storage_pool_by_name(self, name):
        storage_pools = self.restApi.run_pflex('GET',"api/types/StoragePool/instances")
        for storage_pool in storage_pools:
            if storage_pool['name'] == name:
                return storage_pool['id']
            
    
    def get_protection_domain_by_name(self, name):
        protect_domains = self.restApi.run_pflex('GET',"api/types/ProtectionDomain/instances")
        for pd in protect_domains:
            if pd['name'] == name:
                return pd['id']


    def create_nas_server(self,ips, pd_name):
        pst_client = self.get_powerflex_client()
        nas_api = NasServersApi(pst_client)
        protection_domain_id = self.get_protection_domain_by_name(pd_name)
        if len(ips):
            i = 0
            while i<len(ips):
                name = "NAS_test_"+database.generate_random_str(5)
                body = NasServersCreate(name = name,protection_domain_id=protection_domain_id)
                nas_server = nas_api.nas_servers_post(body)
                sql = "insert into pflex_nas_objs (nas_ip, nas_name, nas_id, protection_domain_id) values ( '"+ips[i]+"','"+name+"','"+nas_server.id+"','"+protection_domain_id+"');"
                print(sql)
                database.insert_data(sql)
                i = i+1

    def delete_nas_server(self):
        pst_client = self.get_powerflex_client()
        nas_api = NasServersApi(pst_client)

        sql = "select nas_id from pflex_nas_objs;"
        lst = database.get_data(sql)
        for obj in lst:
            
            nas_api.nas_servers_id_delete(obj[0])
        sql = "delete from pflex_nas_objs;"
        database.delete_data(sql)

    def create_file_interface(self):
        pst_client = self.get_powerflex_client()
        file_interface_api = FileInterfacesApi(pst_client)
        sql = "select * from pflex_nas_objs;"
        lst = database.get_data(sql)
        for i in lst:
            body = FileInterfaceCreate (nas_server_id=i[1],ip_address=i[0],prefix_length=24,vlan_id=251)
            file_interface_api.file_interfaces_post(body)

    def create_smb_server(self):
        pst_client = self.get_powerflex_client()
        smb_server_api = SmbServersApi(pst_client)
        sql = "select * from pflex_nas_objs;"
        lst = database.get_data(sql)
        for i in lst:
            netbios = i[2].split("_")
            body = SmbServerCreate (nas_server_id = i[1],is_standalone=True, netbios_name=netbios[2], workgroup="TEST",local_admin_password="Admin@123")
            smb_server_api.smb_servers_post(body)

    def create_nfs_server(self):
        pst_client = self.get_powerflex_client()
        nfs_server_api = NfsServersApi(pst_client)
        sql = "select * from pflex_nas_objs;"
        lst = database.get_data(sql)
        for i in lst:
            body = NfsServerCreate (nas_server_id = i[1],is_nfsv3_enabled=True,is_nfsv4_enabled=True)
            nfs_server_api.nfs_servers_post(body)

    def create_smb_share(self):
        pst_client = self.get_powerflex_client()
        smb_export_api = SmbSharesApi(pst_client)
        sql = "select filesystem_id, filesystem_name from filesystem_objs;"
        lst = database.get_data(sql)
        for obj in lst:
            path = "/"+obj[1]
            body = SmbShareCreate (file_system_id=obj[0],path=path,name=obj[1],is_abe_enabled=True,is_branch_cache_enabled=True,umask="755",is_continuous_availability_enabled=True,is_encryption_enabled=True)
            smb_export_api.smb_shares_post(body)

            smbpath = "\\\\"+obj[0]+"\\"+obj[1]
            sql = "update filesystem_objs set smbpath = '"+smbpath+"' where filesystem_id = '"+obj[2]+"';"
            #print(sql)
            database.update_data(sql)

    def create_nfs_export(self):
        pst_client = self.get_powerflex_client()
        nfs_export_api = NfsExportsApi(pst_client)
        # sql = "select filesystem_id, filesystem_name from filesystem_objs;"
        sql = "select a.nas_ip, b.filesystem_name,b.filesystem_id from pflex_nas_objs as a join filesystem_objs as b where a.nas_id=b.nas_id;"
        lst = database.get_data(sql)
        for obj in lst:
            path = "/"+obj[1]
            body = NfsExportCreate(file_system_id=obj[2],path=path,name=obj[1],default_access=NFSExportDefaultAccessEnum.ROOT)
            nfs_export_api.nfs_exports_post(body)
            nfs4path = obj[0]+":"+path
            sql = "update filesystem_objs set nfspath = '"+nfs4path+"' where filesystem_id = '"+obj[2]+"';"
            #print(sql)
            database.update_data(sql)

    def create_file_system(self,fsnum, size, storage_pool):
        lst = database.get_data("select nas_id from pflex_nas_objs;")
        pst_client = self.get_powerflex_client()
        filesystem_api = FileSystemsApi(pst_client)
        storage_pool_id = self.get_storage_pool_by_name(storage_pool)
        for nasid in lst:
            i=0
            while i<fsnum:
                if (i % 10) == 0:
                    pst_client = self.get_powerflex_client()
                    filesystem_api = FileSystemsApi(pst_client)
                name = "fs_general_"+database.generate_random_str(5)
                body = FileSystemCreate(name=name,nas_server_id=nasid[0],
                                                        size_total=size*1024*1024*1024,is_async_m_time_enabled=True,
                                                        
                                                        storage_pool_id=storage_pool_id)
                file_system = filesystem_api.file_systems_post(body)

                sql = "insert into filesystem_objs values ('"+nasid[0]+"','"+name+"','"+file_system.id+"','GENERAL','','');"
                print(sql)
                database.insert_data(sql)
                i = i+1

    def delete_file_system(self):
        lst = database.get_data("select filesystem_id from filesystem_objs;")
        pst_client = self.get_powerflex_client()
        filesystem_api = FileSystemsApi(pst_client)

        for fs in lst:
            filesystem_api.file_systems_id_delete(fs[0])
        sql = "delete from filesystem_objs;"
        database.delete_data(sql)

    def delete_file_system_by_rest(self):
        lst2 = database.get_data("select filesystem_id from filesystem_objs;")
        for fs in lst2:
            ret_code = self.restApi.run_pflex('DELETE',"rest/v1/file-systems/{}".format(fs[0]))
            if ret_code == 204: 
                sql = "delete from filesystem_objs where filesystem_id='"+fs[0]+"';"
                database.delete_data(sql)
    
    def delete_nas_server_by_rest(self):
        sql = "select nas_id from pflex_nas_objs;"
        lst = database.get_data(sql)
        for obj in lst:
            ret_code = self.restApi.run_pflex('DELETE',"rest/v1/nas-servers/{}".format(obj[0]))
            if ret_code == 204: 
                sql = "delete from pflex_nas_objs where nas_id='"+obj[0]+"';"
                database.delete_data(sql)   


    def mount_share(self,prefix):
        lst = database.get_data("select VM_IP,TYPE from vm_objs where VM_NAME LIKE '%"+prefix+"%';")
        nfspathlst = database.get_data("select distinct nfspath from filesystem_objs;")
        smbpathlst = database.get_data("select distinct smbpath from filesystem_objs;")
        tasks = []
        i = 0
        for obj in lst:
            if obj[1] == "Linux":
                nfsindex = i%len(nfspathlst)
                cmd = "mkdir -p /tmp/data_0 && mount {} /tmp/data_0".format(nfspathlst[nfsindex][0])
                print("------------")
                print(cmd)
                print("------------")
                thread=Thread(target = self.exec_command,args=(obj[0],cmd,'root','#1Danger0us'))
                thread.start()
                tasks.append(thread)

            elif obj[1] == "Windows":
                smbindex = i%len(smbpathlst)
                cmd = "$net = new-object -ComObject WScript.Network;$net.MapNetworkDrive("'Z:'", "+smbpathlst[smbindex][0]+", $false, "'Administrator'", "'Admin@123'")"
                print("------------")
                print(cmd)
                print("------------")
                thread=Thread(target = self.exec_command,args=(obj[0],cmd,'administrator','Admin@123'))
                thread.start()
                tasks.append(thread)                     
            i = i+1
        
        for t in tasks:
            t.join()

    def mount_share_batch(self,prefix):
        lst = database.get_data("select VM_IP,TYPE from vm_objs where VM_NAME LIKE '%"+prefix+"%';")
        nfspathlst = database.get_data("select distinct nfspath from filesystem_objs;")
        smbpathlst = database.get_data("select distinct smbpath from filesystem_objs;")
        mount_dict = defaultdict(list)
        broker = '172.16.65.3:9092'
        topic = ""
        i = 0
        for obj in lst:
            if obj[1] == "Linux":
                topic = "Linux"
                vm_key = "".join(obj[0].split("."))
                nfsindex = i%len(nfspathlst)
                mount_dict[vm_key].append(nfspathlst[nfsindex][0])
            elif obj[1] == "Windows":
                topic = "Windows"
                vm_key = ".".join(obj[0])
                smbindex = i%len(smbpathlst)
                mount_dict[vm_key].append(smbpathlst[smbindex][0])
            i = i + 1
        producer = MessageProducer(broker,topic)
        # serialized_dict = json.dumps(mount_dict).encode('utf-8')
        headers = [("test","test-share-mount".encode("utf-8"))]
        producer.send_msg(mount_dict,headers = headers)



    def exec_command(self, ip,command,username,password, return_need = True):
        excutor = Executor(ip, username, password)
        excutor.execute(command)



    def ummount_share(self):
        lst = database.get_data("select VM_IP,TYPE from vm_objs;")
        tasks = []
        for obj in lst:
            if obj[1] == "Linux":
                cmd = "umount -a"
                thread=Thread(target = self.exec_command,args=(obj[0],cmd,'root','#1Danger0us'))
                thread.start()
                tasks.append(thread)

            elif obj[1] == "Windows":
                cmd = "`(Get-CimInstance -Class Win32_NetworkConnection).LocalName | ForEach-Object {net use $_ /delete /y}`"
                thread=Thread(target = self.exec_command,args=(obj[0],cmd,'administrator','Admin@123'))
                thread.start()
                tasks.append(thread)                     
        
        for t in tasks:
            t.join()
        sleep(120)
