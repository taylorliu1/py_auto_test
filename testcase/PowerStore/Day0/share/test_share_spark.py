import re
from PowerStore.share.shareImpl import ShareImpl
import os
from common.databases.database import database
from common.monitor.node_exporter_deployment import NodeHelper
from utils.os.Esxi import EsxiExecutor
from utils.os.Linux import Executor
from utils.vsphere.VMUtil import VM
import allure
import time
from utils.kafka.kafka_agent.test_file_share import FileShare

from utils.workload.vdbench.vdbench import Vdbench
class Test_Setup:
    @allure.title("test share day0")
    @allure.description("test share day0 description")
    def setup_class(self):
        print("create tables if not exist")
        self.share = ShareImpl()
        database.init_DB()
        self.vm = VM()
    
    def teardown_class(self):
        print("teardown test case")


    def init(self, config,jsons):
        print("init share dabase")
        trident_ip = config['PowerStore']['share']['url']
        user = config['PowerStore']['share']['user']
        pwd = config['PowerStore']['share']['pwd']
        sql = "insert into trident_objs (ip, user, password) values ( '"+trident_ip+"','"+user+"','"+pwd+"');"
        try:
            database.insert_data(sql)
        except Exception as e:
            print (e)
        print("init vsphere dabase")
        self.init_vcenter_info(jsons)
        
    def init_vcenter_info(self,jsons):
        os.environ["GOVC_URL"] = jsons["vsphere"]["vcenter"]
        os.environ["GOVC_USERNAME"] = jsons["vsphere"]["user"]
        os.environ["GOVC_PASSWORD"] = jsons["vsphere"]["password"]
        os.environ["GOVC_INSECURE"] = jsons["vsphere"]["insecure"]
        os.environ["GOVC_DATACENTER"] = jsons["vsphere"]["datacenter"]
        os.environ["GOVC_RESOURCE_POOL"] = jsons["vsphere"]["respool"]
        self.esxiExecutor = EsxiExecutor(jsons["vsphere"]["vcenter"],jsons["vsphere"]["user"],jsons["vsphere"]["password"])
        
               
    def create_nas(self,config):      
        ips = config["PowerStore"]["NAS"]["nasserverip"]
        self.share.create_nas_server(ips)
            # captured = capsys.readouterr()
            # print (captured.out)
            # print (captured.err)
        # assert captured.out == "PASS\n"

    def create_file_interface(self):
        self.share.create_file_interface()

    def create_file_system(self,config):
        fsnum = config["PowerStore"]["NAS"]["fsnum"]
        self.share.create_file_system(fsnum, type="general")

    def create_nfs_server(self):
        self.share.create_nfs_server()

    def create_nfs_export(self):
         self.share.create_nfs_export()

    def create_smb_server(self):
        self.share.create_smb_server()

    def create_smb_share(self):
         self.share.create_smb_share()
    
    def mount_nfs_datastore(self,config):
        esxi_hosts = config["PowerStore"]["esxi_hosts"]
        self.esxiExecutor.mount_nfs_datastore(esxi_hosts)

    def clone_vms(self,jsons):
        ip_range = jsons["ip"]["ens224"]["range"]
        winbase = jsons["vm"]["winbase"]
        cenbase = jsons["vm"]["cenbase"]
        os = jsons["vm"]["os"]
        net = jsons["ip"]["ens224"]["net"]
        custmask = jsons["ip"]["ens224"]["mask"]
        custgw = jsons["ip"]["ens224"]["gateway"]
        prefix= jsons["vm"]["nameprefix"]
        datastore = jsons["vsphere"]["datastore"]
        # Get datastore info
        print("start cloning vms...")
        self.vm.clone_vm_on_vmfs(ip_range,winbase,cenbase,net,custmask,custgw,prefix,datastore)
        sql = "select count(*) from vm_objs;"
        count = database.get_data(sql)[0][0]
        assert count != 0
        print("clone vms finished!")


    def install_agent(self,jsons):
        prefix= jsons["vm"]["nameprefix"]
        sql = "select type, vm_ip from vm_objs where VM_NAME LIKE '%"+prefix+"%';"
        vms = database.get_data(sql)
        for vm in vms:
            if vm[0] == "Linux":
                NodeHelper.deploy_kafka_agent(vm[1],"root","Admin@123")
            else:
                NodeHelper.upload_file_windows(vm[1], "administrator", "Admin@123","kafka_agent.zip")

    def mount_share(self,jsons):
        prefix= jsons["vm"]["nameprefix"]
        mount_dict = self.share.mount_share_batch(prefix)
        return mount_dict

    def spark_file(self,fileinfos,mount_dict):
        num = fileinfos["file"]["num"]
        retry = fileinfos["file"]["retry"]
        duration = fileinfos["file"]["duration"]
        depth = fileinfos["file"]["depth"]
        size = fileinfos["file"]["size"]
        os_type = fileinfos["file"]["os_type"]
        FileShare().test_file_share(num, retry, duration, depth, size, os_type, mount_dict)



    def test_share(self,jsons,config,fileinfos):
        self.init(config,jsons)
        self.init_vcenter_info(jsons)
        with allure.step("create NAS server"):  
            self.create_nas(config)
        with allure.step("create File system"):
            self.create_file_system(config)
        with allure.step("create File interface"):
            self.create_file_interface()
        with allure.step("create nfs server"):
            self.create_nfs_server()
        with allure.step("create nfs export"):
            self.create_nfs_export()
        with allure.step("create smb server"):
            self.create_smb_server()
        with allure.step("create smb share"):
            self.create_smb_share()   
        with allure.step("clone vms"):
            time.sleep(10)
            self.clone_vms(jsons)
        with allure.step("install agent"):
            self.install_agent(jsons)
        with allure.step("mount share"):
            mount_dict = self.mount_share(jsons)
        with allure.step("write hole file to the mountpoint"):
            self.spark_file(fileinfos,mount_dict)


  
class Test_Clean:
    def setup_class(self):
        self.share = ShareImpl()
        database.init_DB()
        self.vm = VM()

    def init_vcenter_info(self,jsons):
        os.environ["GOVC_URL"] = jsons["vsphere"]["vcenter"]
        os.environ["GOVC_USERNAME"] = jsons["vsphere"]["user"]
        os.environ["GOVC_PASSWORD"] = jsons["vsphere"]["password"]
        os.environ["GOVC_INSECURE"] = jsons["vsphere"]["insecure"]
        os.environ["GOVC_DATACENTER"] = jsons["vsphere"]["datacenter"]
        os.environ["GOVC_RESOURCE_POOL"] = jsons["vsphere"]["respool"]
        self.esxiExecutor = EsxiExecutor(jsons["vsphere"]["vcenter"],jsons["vsphere"]["user"],jsons["vsphere"]["password"])

    def delete_vm(self,jsons):
        prefix= jsons["vm"]["nameprefix"]
        self.vm.delete_vm(prefix)

    def delete_ds(self, config):
        time.sleep(10)
        hosts = config["PowerStore"]["esxi_hosts"]
        for host in hosts:
            self.esxiExecutor.delete_nfs_datastore(host)

    def delete_file_system(self):
        self.share.delete_file_system_by_rest()

    def delete_nas_server(self):
        self.share.delete_nas_server()

    def test_nfs_clean(self,jsons,config):
        self.init_vcenter_info(jsons)
        self.delete_vm(jsons)
        # self.delete_ds(config)
        self.delete_file_system()
        self.delete_nas_server()