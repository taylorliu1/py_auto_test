import os
import time
from common.databases.database import database
from utils.vsphere.VMUtil import VM
from PowerStore.VoD.vodlmpl import VoDImpl

class Test_Setup:

    def setup_class(self):
        print("create tables if not exist")
        self.vod = VoDImpl()
        database.init_DB()
        self.vm = VM()

    def teardown_class(self):
        print("teardown test case")
        # self.vm.delete_vm()

    def test_init(self, config, jsons):
        print("init share dabase")
        print("init vsphere dabase")
        self.init_vcenter_info(jsons)

    def init(self, config, jsons):
        print("init vod dabase")
        trident_ip = config['PowerStore']['taylor']['url']
        user = config['PowerStore']['taylor']['user']
        pwd = config['PowerStore']['taylor']['pwd']
        sql = "insert into trident_objs (ip, user, password) values ( '"+trident_ip+"','"+user+"','"+pwd+"');"
        database.insert_data(sql)
        print("init vsphere dabase")
        self.init_vcenter_info(jsons)

    def init_vcenter_info(self, jsons):
        os.environ["GOVC_URL"] = jsons["vsphere"]["vcenter"]
        os.environ["GOVC_USERNAME"] = jsons["vsphere"]["user"]
        os.environ["GOVC_PASSWORD"] = jsons["vsphere"]["password"]
        os.environ["GOVC_INSECURE"] = jsons["vsphere"]["insecure"]
        os.environ["GOVC_DATACENTER"] = jsons["vsphere"]["datacenter"]
        os.environ["GOVC_DATASTORE"] = jsons["vsphere"]["datastore"]
        os.environ["GOVC_RESOURCE_POOL"] = jsons["vsphere"]["respool"]

    def test_vod(self, jsons, config):
        self.init(config, jsons)
        self.init_vcenter_info(jsons)
        # create nas server
        ips = config["PowerStore"]["NAS"]["nasserverip"]
        self.vod.create_nas_server(ips)
        # create file interface
        self.vod.create_file_interface()
        # create SMB server
        self.vod.create_smb_server()
        # create NFS server
        self.vod.create_nfs_server()
        # create filesystem
        fs_num = config["PowerStore"]["NAS"]["fsnum"]
        self.vod.create_file_system(fs_num=fs_num)
        # create smb share
        self.vod.create_smb_share()
        # create NFS export
        self.vod.create_nfs_export()
        # clone vm
        ips = jsons["ip"]["ens224"]["pool"][0]
        vm_num = jsons["vm"]["num"]
        prefix = jsons["vm"]["nameprefix"]
        vm_base = jsons["vm"]["base"]
        ip_list = self.vm.CreateIP(ips, vm_num)
        vm_names = self.vm.create_names(vm_num, prefix)
        dict_vm = dict(zip(vm_names, ip_list))
        for name, ip in dict_vm.items():
            sql_update_obj = "insert into vm_objs (vm_name, vm_ip) values ( '" + name + "','" + ip + "');"
            database.insert_data(sql_update_obj)

        for name, ip in dict_vm.items():
            self.vm.clone_vm_on_default_datastore(name=name, ip=ip, vm_base=vm_base)

        time.sleep(60)

        # create mount path
        cmd_mount_path = "mkdir /mnt/test"
        print(cmd_mount_path)
        lst = database.get_data("select VM_IP from vm_objs;")
        for obj in lst:
            res = self.vod.exec_cmd(ip=obj[0], command=cmd_mount_path, username="root", password="Admin@123")
            print(res)

        mount_info = database.get_data("select nfspath from filesystem_objs;")
        mount_list = list()
        for mount in mount_info:
            mount_list.append(mount[0])
        vm_ip = database.get_data("select VM_IP from vm_objs;")
        ip_list = list()
        for vm in vm_ip:
            ip_list.append(vm[0])
        dict_mount_point = dict(zip(mount_list, ip_list))
        # "select a.nas_ip, b.filesystem_name,b.filesystem_id from nas_objs as a join filesystem_objs as b where a.nas_id=b.nas_id;"
        for mount_point, ip in dict_mount_point.items():
            cmd_mount = "mount {0} /mnt/test && mkdir /mnt/test/frame/".format(mount_point)
            res = self.vod.exec_cmd(ip=ip, command=cmd_mount, username="root", password="Admin@123")
            print(res)
            cmd_frame = "nohup /root/frametest -w 4k -t 4 -d 10 -n 5000000 -l 500000 -f 24 /mnt/test/frame > myout.file 2>&1 &"
            res = self.vod.exec_cmd(ip=ip, command=cmd_frame, username="root", password="Admin@123")
            print(res)



