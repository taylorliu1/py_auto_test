import base64
from time import sleep
from threading import Thread
import random
import time
from common.databases.database import database
from utils.vsphere.CmdUtil import CMD
from utils.os.Linux import Executor
from PowerStore.share.share import ShareBase
from PowerStore.prime.swagger_client.configuration import Configuration
from PowerStore.prime.swagger_client.api_client import ApiClient
from PowerStore.prime.swagger_client.api.nas_server_api import NasServerApi
from PowerStore.prime.swagger_client.models.nas_server_create import NasServerCreate
from PowerStore.prime.swagger_client.api.file_interface_api import FileInterfaceApi
from PowerStore.prime.swagger_client.models.file_interface_create import FileInterfaceCreate
from PowerStore.prime.swagger_client.api.smb_server_api import SmbServerApi
from PowerStore.prime.swagger_client.models.smb_server_create import SmbServerCreate
from PowerStore.prime.swagger_client.api.nfs_server_api import NfsServerApi
from PowerStore.prime.swagger_client.models.nfs_server_create import NfsServerCreate
from PowerStore.prime.swagger_client.api.smb_share_api import SmbShareApi
from PowerStore.prime.swagger_client.models.smb_share_create import SmbShareCreate
from PowerStore.prime.swagger_client.api.nfs_export_api import NfsExportApi
from PowerStore.prime.swagger_client.models.nfs_export_create import NfsExportCreate
from PowerStore.prime.swagger_client.api.file_system_api import FileSystemApi
from PowerStore.prime.swagger_client.models.file_system_create import FileSystemCreate
from PowerStore.prime.swagger_client.models.nfs_export_default_access_enum import NFSExportDefaultAccessEnum



class VoDImpl(ShareBase):
    def get_trident_client(self):
        lst = database.get_data("select ip,user,password from trident_objs;")
        ip = lst[0][0]
        user = lst[0][1]
        passwd = lst[0][2]

        configuration = Configuration()
        configuration.host = "https://" + ip + "/api/rest"
        configuration.username = user
        configuration.password = passwd
        configuration.verify_ssl = False
        credentials = user + ':' + passwd
        token = base64.b64encode(credentials.encode())
        tclient = ApiClient(configuration=configuration, header_name="Authorization",
                            header_value='Basic ' + token.decode('utf-8'))
        return tclient

    def create_nas_server(self, ips):
        pst_client = self.get_trident_client()
        nas_api = NasServerApi(pst_client)

        ips = ips.split(",")
        if len(ips):
            i = 0
            while i < len(ips):
                name = "VoD_test_" + database.generate_random_str(5)
                body = NasServerCreate(name=name)

                nas_server = nas_api.nas_server_post(body)
                sql = "insert into nas_objs (nas_ip, nas_name, nas_id) values ( '" + ips[
                    i] + "','" + name + "','" + nas_server.id + "');"
                print(sql)
                database.insert_data(sql)
                i = i + 1

    def delete_nas_server(self):
        pst_client = self.get_trident_client()
        nas_api = NasServerApi(pst_client)

        sql = "select nas_id from nas_objs;"
        lst = database.get_data(sql)
        for obj in lst:
            nas_api.nas_server_id_delete(obj[0])

    def create_file_interface(self):
        pst_client = self.get_trident_client()
        file_interface_api = FileInterfaceApi(pst_client)
        sql = "select * from nas_objs;"
        lst = database.get_data(sql)
        for i in lst:
            body = FileInterfaceCreate(nas_server_id=i[1], ip_address=i[0], prefix_length=16, vlan_id=3105)
            file_interface_api.file_interface_post(body)

    def create_smb_server(self):
        pst_client = self.get_trident_client()
        smb_server_api = SmbServerApi(pst_client)
        sql = "select * from nas_objs;"
        lst = database.get_data(sql)
        for i in lst:
            netbios = i[2].split("_")
            body = SmbServerCreate(nas_server_id=i[1], is_standalone=True, netbios_name=netbios[2], workgroup="TEST",
                                   local_admin_password="Admin@123")
            smb_server_api.smb_server_post(body)

    def create_nfs_server(self):
        pst_client = self.get_trident_client()
        nfs_server_api = NfsServerApi(pst_client)
        sql = "select * from nas_objs;"
        lst = database.get_data(sql)
        for i in lst:
            body = NfsServerCreate(nas_server_id=i[1], is_nfsv3_enabled=True, is_nfsv4_enabled=True)
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
        sql = "select a.nas_ip, b.filesystem_name,b.filesystem_id from nas_objs as a join filesystem_objs as b where a.nas_id=b.nas_id;"
        lst = database.get_data(sql)
        for obj in lst:
            path = "/" + obj[1]
            body = NfsExportCreate(file_system_id=obj[2], path=path, name=obj[1],
                                   default_access=NFSExportDefaultAccessEnum.ROOT)
            nfs_export_api.nfs_export_post(body)
            nfs4path = obj[0] + ":" + path
            sql = "update filesystem_objs set nfspath = '" + nfs4path + "' where filesystem_id = '" + obj[2] + "';"
            database.update_data(sql)

    def create_file_system(self, fs_num):
        lst = database.get_data("select nas_id from nas_objs;")
        pst_client = self.get_trident_client()
        filesystem_api = FileSystemApi(pst_client)
        i = 0
        while i < fs_num:
            index = i % len(lst)
            name = "VoD_" + database.generate_random_str(5)
            body = FileSystemCreate(name=name, nas_server_id=lst[index][0],
                                    size_total=256 * 1024 * 1024 * 1024 * 1024, is_async_m_time_enabled=True)
            file_system = filesystem_api.file_system_post(body)
            sql = "insert into filesystem_objs values ('" + lst[index][0] + "','" + name + "','" + file_system.id + \
                  "', 'General', '' ,''); "
            print(sql)
            database.insert_data(sql)
            i = i + 1
        # sql = "insert into filesystem_objs values ('" + nasid[
        #         #             0] + "','" + name + "','" + file_system.id + "','VMWARE','','');"
        #     i = 0
        #     while i < fsnum:
        #         name = "VoD_" + database.generate_random_str(5)
        #         body = FileSystemCreate(name=name, nas_server_id=nasid[0],
        #                                 size_total=256 * 1024 * 1024 * 1024 * 1024, is_async_m_time_enabled=True,
        #                                 host_io_size=hostiosize[random.randint(0, (len(hostiosize) - 1))],
        #                                 config_type=FileSystemConfigTypeEnum.VMWARE)
        #         file_system = filesystem_api.file_system_post(body)
        #         sql = "insert into filesystem_objs values ('" + nasid[
        #             0] + "','" + name + "','" + file_system.id + "','VMWARE','','');"
        #         print(sql)
        #         database.insert_data(sql)
        #         i = i + 1

    def delete_file_system(self):
        lst = database.get_data("select filesystem_id from filesystem_objs;")
        pst_client = self.get_trident_client()
        filesystem_api = FileSystemApi(pst_client)

        for fs in lst:
            filesystem_api.file_system_id_delete(fs[0])

    def mount_share(self):
        lst = database.get_data("select VM_IP,TYPE from vm_objs;")
        nfs_path_lst = database.get_data("select distinct nfspath from filesystem_objs;")
        smb_path_lst = database.get_data("select distinct smbpath from filesystem_objs;")
        tasks = []
        i = 0
        for obj in lst:
            if obj[1] == "Linux":
                nfs_index = i % len(nfs_path_lst)
                cmd = "mkdir -p /tmp/data_%d && mount %s /tmp/data_%d".format(i, nfs_path_lst[nfs_index], i)
                print("------------")
                print(cmd)
                print("------------")
                thread = Thread(target=self.exec_command, args=(obj[0], cmd, 'root', 'Admin@123'))
                thread.start()
                tasks.append(thread)

            elif obj[1] == "Windows":
                smb_index = i % len(smb_path_lst)
                cmd = "$net = new-object -ComObject WScript.Network;$net.MapNetworkDrive("'Z:'", " + smb_path_lst[
                    smb_index] + ", $false, "'Administrator'", "'Admin@123'")"
                print("------------")
                print(cmd)
                print("------------")
                thread = Thread(target=self.exec_command, args=(obj[0], cmd, 'administrator', 'Admin@123'))
                thread.start()
                tasks.append(thread)
            i = i + 1

        for t in tasks:
            t.join()
        sleep(120)

    def ummount_share(self):
        lst = database.get_data("select VM_IP,TYPE from vm_objs;")
        tasks = []
        for obj in lst:
            if obj[1] == "Linux":
                cmd = "umount -a"
                thread = Thread(target=self.exec_command, args=(obj[0], cmd, 'root', 'Admin@123'))
                thread.start()
                tasks.append(thread)

            elif obj[1] == "Windows":
                cmd = "`(Get-CimInstance -Class Win32_NetworkConnection).LocalName | ForEach-Object {net use $_ /delete /y}`"
                thread = Thread(target=self.exec_command, args=(obj[0], cmd, 'administrator', 'Admin@123'))
                thread.start()
                tasks.append(thread)

        for t in tasks:
            t.join()
        sleep(120)

    def exec_cmd(self, ip, command, username, password, return_need=True):
        excutor = Executor(ip, username, password)
        excutor.execute(command)
        # client = paramiko.SSHClient()
        # client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # try:
        #     client.connect(ip, username, password, timeout=30)
        # except:
        #     print("connect to {} error!!!".format(ip))
        #     return False
        # stdin, stdout, stderr = client.exec_command(command)
        # if return_need:
        #     out = stdout.read().decode().strip()
        #     client.close()
        #     return out
        # client.close()
