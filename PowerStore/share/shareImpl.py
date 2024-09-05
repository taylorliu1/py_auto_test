import base64
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from sys import prefix

from PowerStore.share.share import ShareBase
from PowerStore.prime.swagger_client.configuration import Configuration
from PowerStore.prime.swagger_client.api_client import ApiClient
from PowerStore.prime.swagger_client.api.nas_server_api import NasServerApi
from PowerStore.prime.swagger_client import NasServerCreate
from common.databases.database import database
from PowerStore.prime.swagger_client.models.nas_server_create import NasServerCreate
from PowerStore.prime.swagger_client.models.file_interface_create import FileInterfaceCreate
from PowerStore.prime.swagger_client import FileInterfaceApi
from PowerStore.prime.swagger_client.api.smb_share_api import SmbShareApi
from PowerStore.prime.swagger_client.models.smb_share_create import SmbShareCreate
from PowerStore.prime.swagger_client import SmbServerApi
from PowerStore.prime.swagger_client.models.smb_server_create import SmbServerCreate
from PowerStore.prime.swagger_client import NfsServerApi
from PowerStore.prime.swagger_client.models.nfs_server_create import NfsServerCreate
from PowerStore.prime.swagger_client.models.nfs_export_create import NfsExportCreate
from PowerStore.prime.swagger_client.api.nfs_export_api import NfsExportApi
from PowerStore.prime.swagger_client.models.nfs_export_default_access_enum import NFSExportDefaultAccessEnum
from PowerStore.prime.swagger_client.api.file_system_api import FileSystemApi
from PowerStore.prime.swagger_client.models.file_system_create import FileSystemCreate
from PowerStore.prime.swagger_client.models.file_system_config_type_enum import FileSystemConfigTypeEnum
from PowerStore.prime.swagger_client.models.file_system_host_io_size_enum import FileSystemHostIoSizeEnum
from threading import Thread
from time import sleep
from utils.vsphere.VMUtil import VM
from utils.kafka.kafkaProducerUtil import MessageProducer

from utils.os.Linux import Executor
from utils.restapi import APIRequest


class ShareImpl(ShareBase):

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

    def create_nas_server(self,ips):
        pst_client = self.get_trident_client()
        nas_api = NasServerApi(pst_client)
        if len(ips):
            i = 0
            while i<len(ips):
                name = "NAS_test_"+database.generate_random_str(5)
                body = NasServerCreate(name = name)

                nas_server = nas_api.nas_server_post(body)
                sql = "insert into nas_objs (nas_ip, nas_name, nas_id) values ( '"+ips[i]+"','"+name+"','"+nas_server.id+"');"
                print(sql)
                database.insert_data(sql)
                i = i+1

    def delete_nas_server(self):
        pst_client = self.get_trident_client()
        nas_api = NasServerApi(pst_client)

        sql = "select nas_id from nas_objs;"
        lst = database.get_data(sql)
        for obj in lst:
            
            nas_api.nas_server_id_delete(obj[0])
        sql = "delete from nas_objs;"
        database.delete_data(sql)

    def create_file_interface(self):
        pst_client = self.get_trident_client()
        file_interface_api = FileInterfaceApi(pst_client)
        sql = "select * from nas_objs;"
        lst = database.get_data(sql)
        for i in lst:
            body = FileInterfaceCreate (nas_server_id=i[1],ip_address=i[0],prefix_length=16,vlan_id=3105)
            file_interface_api.file_interface_post(body)

    def create_smb_server(self):
        pst_client = self.get_trident_client()
        smb_server_api = SmbServerApi(pst_client)
        sql = "select * from nas_objs;"
        lst = database.get_data(sql)
        for i in lst:
            netbios = i[2].split("_")
            body = SmbServerCreate (nas_server_id = i[1],is_standalone=True, netbios_name=netbios[2], workgroup="TEST",local_admin_password="Admin@123")
            smb_server_api.smb_server_post(body)

    def create_nfs_server(self):
        pst_client = self.get_trident_client()
        nfs_server_api = NfsServerApi(pst_client)
        sql = "select * from nas_objs;"
        lst = database.get_data(sql)
        for i in lst:
            body = NfsServerCreate (nas_server_id = i[1],is_nfsv3_enabled=True,is_nfsv4_enabled=True)
            nfs_server_api.nfs_server_post(body)

    def create_smb_share(self):
        pst_client = self.get_trident_client()
        smb_export_api = SmbShareApi(pst_client)
        sql = "select a.nas_ip, b.filesystem_name,b.filesystem_id from nas_objs as a join filesystem_objs as b where a.nas_id=b.nas_id;"
        lst = database.get_data(sql)
        for obj in lst:
            path = "/" + obj[1]
            body = SmbShareCreate(file_system_id=obj[2], path=path, name=obj[1], is_abe_enabled=True,
                                  is_branch_cache_enabled=True, umask="755", is_continuous_availability_enabled=True,
                                  is_encryption_enabled=True)
            smb_export_api.smb_share_post(body)

            smbpath = "\\\\" + obj[0] + "\\" + obj[1]
            sql = "update filesystem_objs set smbpath = '" + smbpath + "' where filesystem_id = '" + obj[2] + "';"
            database.update_data(sql)
            
    def create_nfs_export(self):
        pst_client = self.get_trident_client()
        nfs_export_api = NfsExportApi(pst_client)
        # sql = "select filesystem_id, filesystem_name from filesystem_objs;"
        sql = "select a.nas_ip, b.filesystem_name,b.filesystem_id from nas_objs as a join filesystem_objs as b where a.nas_id=b.nas_id;"
        lst = database.get_data(sql)
        with ThreadPoolExecutor(max_workers=10) as executor:
            for obj in lst:
                executor.submit(self.async_create_nfs_export,nfs_export_api, obj)

    def async_create_nfs_export(self, nfs_export_api, obj):
        path = "/"+obj[1]
        body = NfsExportCreate(file_system_id=obj[2],path=path,name=obj[1],default_access=NFSExportDefaultAccessEnum.ROOT)
        nfs_export_api.nfs_export_post(body)
        nfs4path = obj[0]+":"+path
        sql = "update filesystem_objs set nfspath = '"+nfs4path+"' where filesystem_id = '"+obj[2]+"';"
            #print(sql)
        database.update_data(sql)

    def create_file_system(self,fsnum,size=256*1024, type="vmware"):
        lst = database.get_data("select nas_id from nas_objs;")
        pst_client = self.get_trident_client()
        filesystem_api = FileSystemApi(pst_client)
        hostiosize = [FileSystemHostIoSizeEnum._8K,FileSystemHostIoSizeEnum._16K,FileSystemHostIoSizeEnum._32K,FileSystemHostIoSizeEnum._64K]
        for nasid in lst:
            i=0
            with ThreadPoolExecutor(max_workers=10) as executor:
                while i<fsnum:
                    if type == "general":
                        executor.submit(self.sync_create_fs_general,size, filesystem_api, nasid)
                    else:
                        index = i % len(hostiosize)
                        executor.submit(self.async_create_fs_vmware,size, filesystem_api, hostiosize, nasid, index)
                    i += 1    

    def async_create_fs_vmware(self, size, filesystem_api, hostiosize, nasid, index):
        name = "fs_vmware_"+database.generate_random_str(5)
        body = FileSystemCreate(name=name,nas_server_id=nasid[0],
                                                        size_total=size*1024*1024*1024,is_async_m_time_enabled=True,
                                                        host_io_size=hostiosize[index],
                                                        config_type=FileSystemConfigTypeEnum.VMWARE)
        file_system = filesystem_api.file_system_post(body)

        sql = "insert into filesystem_objs values ('"+nasid[0]+"','"+name+"','"+file_system.id+"','VMWARE','','');"
        print(sql)
        database.insert_data(sql)

    def sync_create_fs_general(self, size, filesystem_api, nasid):
        name = "fs_general_"+database.generate_random_str(5)
        body = FileSystemCreate(name=name, nas_server_id=nasid[0],
                            size_total=size*1024*1024*1024, is_async_m_time_enabled=True)
        file_system = filesystem_api.file_system_post(body)
        sql = "insert into filesystem_objs values ('"+nasid[0]+"','"+name+"','"+file_system.id+"','General','','');"
        print(sql)
        database.insert_data(sql)

    def delete_file_system(self):
        lst = database.get_data("select filesystem_id from filesystem_objs;")
        pst_client = self.get_trident_client()
        filesystem_api = FileSystemApi(pst_client)

        for fs in lst:
            filesystem_api.file_system_id_delete(fs[0])
        sql = "delete from filesystem_objs;"
        database.delete_data(sql)

    def delete_file_system_by_rest(self):
        lst = database.get_data("select ip,user,password from trident_objs;")
        ip = lst[0][0]
        user = lst[0][1]
        passwd = lst[0][2]
        restApi = APIRequest(ip,user,passwd)
        lst2 = database.get_data("select filesystem_id from filesystem_objs;")
        with ThreadPoolExecutor(max_workers=10) as executor:
            for fs in lst2:
                executor.submit(self.async_delete_fs_by_rest,restApi, fs)

    def async_delete_fs_by_rest(self, restApi, fs):
        ret_code = restApi.run('DELETE',"api/rest/file_system/{}".format(fs[0]))
        if ret_code == 204: 
            sql = "delete from filesystem_objs where filesystem_id='"+fs[0]+"';"
            database.delete_data(sql)


    def mount_share(self,prefix):
        lst = database.get_data("select VM_IP,TYPE from vm_objs where VM_NAME LIKE '%"+prefix+"%';")
        nfspathlst = database.get_data("select distinct nfspath from filesystem_objs;")
        smbpathlst = database.get_data("select distinct smbpath from filesystem_objs;")
        broker = '172.16.20.12:9092'
        i = 0
        for obj in lst:
            index = VM().ip2int(obj[0])
            topic = 'py-test-topic'+str(index)
            message_producer = MessageProducer(broker,topic)
            if obj[1] == "Linux":
                nfsindex = i%len(nfspathlst)
                data = "mkdir -p /tmp/data_"+str(i)+" && mount "+nfspathlst[nfsindex]+" /tmp/data_"+str(i)
                path = "/tmp/data_"+str(i)
                data1 = "sed -i 's%path%"+path+"%g' /root/vdbench50407/vd/create_files"
                run_vd = "cd /root/vdbench50407/vd && ./vdbench -f create_files"
                resp=message_producer.send_msg(data)
                print(resp)
                sleep(10)
                resp1=message_producer.send_msg(data1)
                print(resp1)
                resp2=message_producer.send_msg(run_vd)
                print(resp2)
                
                
            elif obj[1] == "Windows":
                smbindex = i%len(smbpathlst)
                data = "net use T: "+smbpathlst[smbindex]+" Admin@123 /user:administrator /persistent:yes && C:\\vdbench50407\\vd\\vdbench -f C:\\vdbench50407\\vd\\create_files"
                resp=message_producer.send_msg(data)
                print(resp)
            i = i+1
    
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
        return mount_dict
        

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
