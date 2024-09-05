import os
import time
import subprocess
from common.databases.database import database
from utils.vsphere.VMUtil import VM
from PowerStore.VoD.vodlmpl import VoDImpl
from common.monitor.node_exporter_deployment import NodeHelper
import allure


class Test_Setup:
    def __init__(self):
        self.vm = None
        self.vod = None

    @allure.title("test VoD day1")
    @allure.description("test VoD day1 longevity description")
    def setup_class(self):
        print("create tables if not exist")
        self.vod = VoDImpl()
        database.init_DB()
        self.vm = VM()

    def teardown_class(self):
        print("teardown test case")

    def init(self, config, jsons):
        print("init vod dabase")
        trident_ip = config['PowerStore']['array']['url']
        user = config['PowerStore']['array']['user']
        pwd = config['PowerStore']['array']['pwd']
        sql = "insert into trident_objs (ip, user, password) values ( '" + trident_ip + "','" + user + "','" + pwd + "');"
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

    def create_nas(self, config):
        ips = config["PowerStore"]["NAS"]["nasserverip"]
        self.vod.create_nas_server(ips)

    def create_file_interface(self):
        self.vod.create_file_interface()

    def create_smb_server(self):
        self.vod.create_smb_server()

    def create_nfs_server(self):
        self.vod.create_nfs_server()

    def create_file_system(self, config):
        fs_num = config["PowerStore"]["NAS"]["fsnum"]
        self.vod.create_file_system(fs_num)

    def create_nfs_export(self):
        self.vod.create_nfs_export()

    def clone_vm(self, jsons):
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

    def run_workload(self):
        cmd_mount_path = "mkdir /mnt/test"
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
        for mount_point, ip in dict_mount_point.items():
            cmd_mount = "mount {0} /mnt/test && mkdir /mnt/test/frame/".format(mount_point)
            res = self.vod.exec_cmd(ip=ip, command=cmd_mount, username="root", password="Admin@123")
            print(res)
            cmd_frame = "nohup /root/frametest -w 4k -t 10 -d 10 -n 50000 -f 24 /mnt/test/frame > myout.file 2>&1 &"
            res = self.vod.exec_cmd(ip=ip, command=cmd_frame, username="root", password="Admin@123")
            print(res)

        # waiting for flushing data
        time.sleep(360)

        for ip in dict_mount_point.values():
            cmd_reboot = "reboot -f"
            res = self.vod.exec_cmd(ip=ip, command=cmd_reboot, username="root", password="Admin@123")
            print(res)

        # waiting for vm restart
        time.sleep(360)

        for mount_point, ip in dict_mount_point.items():
            cmd_mount = "mount {0} /mnt/test".format(mount_point)
            res = self.vod.exec_cmd(ip=ip, command=cmd_mount, username="root", password="Admin@123")
            print(res)
            cmd_frame = "nohup /root/frametest -r -s -z 1024 -t 10 -n 1440 -f 24 -q 10 /mnt/test/frame >> myout.file 2>&1 &"
            res = self.vod.exec_cmd(ip=ip, command=cmd_frame, username="root", password="Admin@123")
            print(res)

    def install_node_exporter(self, jsons, config):
        prefix = jsons["vm"]["nameprefix"]
        sql = "select vm_ip from vm_objs where VM_NAME LIKE '%" + prefix + "%';"
        vms = database.get_data(sql)
        # count = 0
        name = config["PowerStore"]["name"]
        user = jsons["vm"]["user"]
        passwd = jsons["vm"]["passwd"]
        for vm in vms:
            NodeHelper.install_exporter_linux(vm[0], user, passwd)
            export_node = name + "_nfs_" + vm[0]
            NodeHelper.create_pushgateway_cronjob(vm[0], user, passwd, export_node)

    def test_VoD(self, config, jsons):
        self.init(config, jsons)
        self.init_vcenter_info(jsons)
        # 1 create nas server
        with allure.step("create Nas server"):
            self.create_nas(config)
        # 2 create interface
        with allure.step("create file interface"):
            self.create_file_interface()
        # 3 create SMB server
        with allure.step("create smb server"):
            self.create_smb_server()
        # 4 create NFS server
        with allure.step("create nfs server"):
            self.create_nfs_server()
        # 5 create filesystem
        with allure.step("create File system"):
            self.create_file_system(config)
        # 6 create NFS export
        with allure.step("create nfs export"):
            self.create_nfs_export()
        # 7 clone VM
        with allure.step("clone vms"):
            time.sleep(10)
            self.clone_vm(jsons)
        with allure.step("install node exporter"):
            self.install_node_exporter(jsons, config)
        # 8 start frame testing
        with allure.step("start workload"):
            self.run_workload()


class Test_Clean:
    def setup_class(self):
        self.vod = VoDImpl()
        database.init_DB()
        self.vm = VM()

    def init_vcenter_info(self, jsons):
        os.environ["GOVC_URL"] = jsons["vsphere"]["vcenter"]
        os.environ["GOVC_USERNAME"] = jsons["vsphere"]["user"]
        os.environ["GOVC_PASSWORD"] = jsons["vsphere"]["password"]
        os.environ["GOVC_INSECURE"] = jsons["vsphere"]["insecure"]
        os.environ["GOVC_DATACENTER"] = jsons["vsphere"]["datacenter"]
        os.environ["GOVC_RESOURCE_POOL"] = jsons["vsphere"]["respool"]
        # self.esxiExecutor = EsxiExecutor(jsons["vsphere"]["vcenter"], jsons["vsphere"]["user"], jsons["vsphere"]["password"])

    def delete_vm(self, jsons):
        prefix = jsons["vm"]["nameprefix"]
        self.vm.delete_vm(prefix)

    def delete_file_system(self):
        self.vod.delete_file_system_by_rest()

    def delete_nas_server(self):
        self.vod.delete_nas_server()

    def delete_pushgateway_job(self, config):
        enable = config["PowerStore"]["vdbench_vm"]["enable"]
        if not enable:
            return
        name = config["PowerStore"]["name"]
        job = name + "_" + "vod"
        delete_cmd = "curl -X DELETE http://10.226.112.170:31659/metrics/job/{}".format(job)
        subprocess.run(delete_cmd, shell=True)

    def test_vod_clean(self, jsons, config):
        self.init_vcenter_info(jsons)
        self.delete_vm(jsons)
        self.delete_file_system()
        self.delete_nas_server()
        self.delete_pushgateway_job(config)
