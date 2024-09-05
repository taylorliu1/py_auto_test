import re
from PowerFlex.share.shareImpl import ShareImpl
import os
from common.databases.database import database
from common.monitor.node_exporter_deployment import NodeHelper
from utils.os.Esxi import EsxiExecutor
from utils.os.Linux import Executor
from utils.vsphere.VMUtil import VM
import allure
import time

from utils.workload.vdbench.vdbench import Vdbench
class Test_Setup:
    @allure.title("test share day0")
    @allure.description("test share day0 description")
    def setup_class(self):
        print("create tables if not exist")   
        database.init_DB()
        self.vm = VM()
    
    def teardown_class(self):
        print("teardown test case")


    def init(self, config,jsons):
        print("init share dabase")
        pflex_ip = config['PowerFlex']['share']['url']
        user = config['PowerFlex']['share']['user']
        pwd = config['PowerFlex']['share']['pwd']
        sql = "insert into pflex_objs (ip, user, password) values ( '"+pflex_ip+"','"+user+"','"+pwd+"');"
        try:
            database.insert_data(sql)
        except Exception as e:
            print (e)
        self.share = ShareImpl()
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
        ips = config["PowerFlex"]["NAS"]["nasserverip"]
        pd_name = config["PowerFlex"]["NAS"]["pd_name"]
        self.share.create_nas_server(ips,pd_name)
            # captured = capsys.readouterr()
            # print (captured.out)
            # print (captured.err)
        # assert captured.out == "PASS\n"

    def create_file_interface(self):
        self.share.create_file_interface()

    def create_file_system(self,config):
        fsnum = config["PowerFlex"]["NAS"]["fsnum"]
        storage_pool = config["PowerFlex"]["NAS"]["storage_pool"]
        size = config["PowerFlex"]["NAS"]["size"]
        self.share.create_file_system(fsnum,size,storage_pool)

    def create_nfs_server(self):
        self.share.create_nfs_server()

    def create_nfs_export(self):
         self.share.create_nfs_export()
    
    def mount_nfs_datastore(self,config):
        esxi_hosts = config["PowerFlex"]["esxi_hosts"]
        self.esxiExecutor.mount_nfs_datastore(esxi_hosts,"NAS")

    # def clone_vms(self,jsons):
    #     ip_range = jsons["ip"]["ens192"]["range"]
    #     base = jsons["vm"]["base"]
    #     os = jsons["vm"]["os"]
    #     net = jsons["ip"]["ens192"]["net"]
    #     custmask = jsons["ip"]["ens192"]["mask"]
    #     custgw = jsons["ip"]["ens192"]["gateway"]
    #     prefix= jsons["vm"]["nameprefix"]
    #     # Get datastore info
    #     datastore_list = database.get_data("select NFS_datastore from datastore_objs;")
    #     print("start cloning vms...")
    #     self.vm.clone_vm_from_range(ip_range,base,os,net,custmask,custgw,prefix,datastore_list)
    #     sql = "select count(*) from vm_objs;"
    #     count = database.get_data(sql)[0][0]
    #     assert count != 0
    #     print("clone vms finished!")

    def clone_vms(self,jsons):
        ip_range = jsons["ip"]["ens192"]["range"]
        base = jsons["vm"]["base"]
        os = jsons["vm"]["os"]
        net = jsons["ip"]["ens192"]["net"]
        custmask = jsons["ip"]["ens192"]["mask"]
        custgw = jsons["ip"]["ens192"]["gateway"]
        prefix= jsons["vm"]["nameprefix"]
        datastore = jsons["vsphere"]["datastore"]
        # Get datastore info
        # datastore_list = database.get_data("select NFS_datastore from datastore_objs;")
        print("start cloning vms...")
        datastore_list = [(datastore,)]
        self.vm.clone_vm_from_range(ip_range,base,os,net,custmask,custgw,prefix,datastore_list)
        sql = "select count(*) from vm_objs;"
        count = database.get_data(sql)[0][0]
        assert count != 0
        print("clone vms finished!")

    # def clone_vms(self,jsons):
    #     ip_range = jsons["ip"]["ens224"]["range"]
    #     winbase = jsons["vm"]["winbase"]
    #     cenbase = jsons["vm"]["cenbase"]
    #     os = jsons["vm"]["os"]
    #     net = jsons["ip"]["ens224"]["net"]
    #     custmask = jsons["ip"]["ens224"]["mask"]
    #     custgw = jsons["ip"]["ens224"]["gateway"]
    #     prefix= jsons["vm"]["nameprefix"]
    #     datastore = jsons["vsphere"]["datastore"]
    #     # Get datastore info
    #     print("start cloning vms...")
    #     self.vm.clone_vm_on_vmfs(ip_range,winbase,cenbase,net,custmask,custgw,prefix,datastore)
    #     sql = "select count(*) from vm_objs;"
    #     count = database.get_data(sql)[0][0]
    #     assert count != 0
    #     print("clone vms finished!")


    def install_node_exporter_and_agent(self,jsons,config):
        prefix= jsons["vm"]["nameprefix"]
        sql = "select vm_ip from vm_objs where VM_NAME LIKE '%"+prefix+"%';"
        vms = database.get_data(sql)
        name = config["PowerFlex"]["name"]
        for vm in vms:
            # NodeHelper.install_exporter_linux(vm[0],"root","#1Danger0us")
            # export_node = name+"_nfs_"+ vm[0]
            # NodeHelper.create_pushgateway_cronjob(vm[0],"root","#1Danger0us",export_node)
            NodeHelper.deploy_kafka_agent(vm[0],"root","#1Danger0us")

    def mount_share(self,jsons):
        prefix= jsons["vm"]["nameprefix"]
        self.share.mount_share_batch(prefix)

    # def run_vdbench(self,config):
    #     enable = config["PowerStore"]["vdbench_vm"]["enable"]
    #     if not enable:
    #         return
    #     node_list = config["PowerStore"]["vdbench_vm"]["Linux"]
    #     name = config["PowerStore"]["name"]
    #     job_list = ["nfs_datastore_4k","nfs_datastore_64k","nfs_datastore_8k","nfs_datastore_128k"]
    #     job_list = list(map(lambda x:name+"_"+x,job_list))
    #     vdbench = Vdbench()
    #     df = vdbench.repalce_column_with_value("node",["node1","node2","node3","node4"],node_list)
    #     df = vdbench.repalce_column_with_value("job",["4k","64k","8k","128k"],job_list,df)
    #     vdbench.run_vdbench("Linux","run",False,df)
    def run_vdbench(self,config):
        enable = config["PowerFlex"]["vdbench_vm"]["enable"]
        if not enable:
            return
        node_list = config["PowerFlex"]["vdbench_vm"]["Linux"]
        node = node_list[0]
        job = "nfs_share"
        name = config["PowerFlex"]["name"]
        # job_list = ["nvme_vmfs_4k","nvme_vmfs_64k","nvme_vmfs_8k","nvme_vmfs_128k"]
        job_list = [job,job,job,job]
        job_list = list(map(lambda x:name+"_"+x,job_list))
        vdbench = Vdbench()
        df = vdbench.repalce_column_with_value("node",["node1","node2","node3","node4"],[node,node,node,node])
        df = vdbench.repalce_column_with_value("job",["4k","64k","8k","128k"],job_list,df)
        vdbench.run_vdbench("Linux","run",False,df)

    def test_share(self,jsons,config):
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
        # with allure.step("mount nfs datastore"):
        #     self.mount_nfs_datastore(config)        
        with allure.step("clone vms"):
            time.sleep(10)
            self.clone_vms(jsons)
        with allure.step("install node exporter and agent"):
            self.install_node_exporter_and_agent(jsons,config)
        # with allure.step("run vdbench"):
        #     self.run_vdbench(config)
        with allure.step("mount share"):
            self.mount_share(jsons)


  
class Test_Clean:
    def setup_class(self):
        self.share = ShareImpl()
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
        hosts = config["PowerFlex"]["esxi_hosts"]
        for host in hosts:
            self.esxiExecutor.delete_nfs41_datastore(host,"NAS")

    def delete_file_system(self):
        self.share.delete_file_system_by_rest()

    def delete_nas_server(self):
        self.share.delete_nas_server_by_rest()

    def test_nfs_clean(self,jsons,config):
        self.init_vcenter_info(jsons)
        self.delete_vm(jsons)
        self.delete_ds(config)
        self.delete_file_system()
        self.delete_nas_server()



        

