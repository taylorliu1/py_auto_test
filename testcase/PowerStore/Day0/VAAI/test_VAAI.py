import subprocess
from PowerStore.VAAI.shareVAAIImpl import ShareVAAIImpl

import os
from common.databases.database import database
from utils.vsphere.VMUtil import VM
import pytest
import time
import allure
from utils.workload.vdbench.vdbench import Vdbench
from common.monitor.node_exporter_deployment import NodeHelper
from utils.os.Esxi import EsxiExecutor

class Test_Setup:

    def setup_class(self):
        print("create tables if not exist")
        self.share = ShareVAAIImpl()
        database.init_DB()
        self.vm = VM()
    
    def teardown_class(self):
        print("teardown test case")
        # self.vm.delete_vm()

    def test_init(self, config,jsons):
        print("init share dabase")
        print("init vsphere dabase")
        self.init_vcenter_info(jsons)

    def init(self, config,jsons):
        print("init share dabase")
        trident_ip = config['PowerStore']['array']['url']
        user = config['PowerStore']['array']['user']
        pwd = config['PowerStore']['array']['pwd']
        sql = "insert into trident_objs (ip, user, password) values ( '"+trident_ip+"','"+user+"','"+pwd+"');"
        database.insert_data(sql)
        print("init vsphere dabase")
        self.init_vcenter_info(jsons)

    def init_vcenter_info(self,jsons):
        os.environ["GOVC_URL"] = jsons["vsphere"]["vcenter"]
        os.environ["GOVC_USERNAME"] = jsons["vsphere"]["user"]
        os.environ["GOVC_PASSWORD"] = jsons["vsphere"]["password"]
        os.environ["GOVC_INSECURE"] = jsons["vsphere"]["insecure"]
        os.environ["GOVC_DATACENTER"] = jsons["vsphere"]["datacenter"]
        #os.environ["GOVC_DATASTORE"] = jsons["vsphere"]["datastore"]
        os.environ["GOVC_RESOURCE_POOL"] = jsons["vsphere"]["respool"]
        self.esxiExecutor = EsxiExecutor(jsons["vsphere"]["vcenter"],jsons["vsphere"]["user"],jsons["vsphere"]["password"])

    def create_nas(self,config):
        ips = config["PowerStore"]["NAS"]["nasserverip"]
        self.share.create_nas_server(ips)

    def create_file_interface(self):
        self.share.create_file_interface()
    
    def create_smb_server(self):
         self.share.create_smb_server()

    def create_nfs_server(self):
        self.share.create_nfs_server()

    def create_file_system(self,config):
        fsnum = config["PowerStore"]["NAS"]["fsnum"]
        self.share.create_file_system(fsnum)

    def create_nfs_export(self):
        self.share.create_nfs_export()

    def mount_nfs_datastore(self,config):
        esxi_hosts = config["PowerStore"]["esxi_hosts"]
        self.esxiExecutor.mount_nfs_datastore(esxi_hosts,"vaai")

    def clone_vm(self,jsons):
        ip_range = jsons["ip"]["ens224"]["range"]
        base = jsons["vm"]["base"]
        os = jsons["vm"]["os"]
        net = jsons["ip"]["ens224"]["net"]
        custmask = jsons["ip"]["ens224"]["mask"]
        custgw = jsons["ip"]["ens224"]["gateway"]
        prefix= jsons["vm"]["nameprefix"]
        vm_num = jsons["vm"]["num"]
        # Get datastore info
        datastore_list = database.get_data("select NFS_datastore from datastore_objs;")
        print("start cloning vms...")
        self.vm.clone_vm_from_range(ip_range,base,os,net,custmask,custgw,prefix,datastore_list)
        sql = "select count(*) from vm_objs;"
        count = database.get_data(sql)[0][0]
        assert count != 0
        print("clone vms finished!")

    def run_vdbench(self,config):
        enable = config["PowerStore"]["vdbench_vm"]["enable"]
        if not enable:
            return
        node_list = config["PowerStore"]["vdbench_vm"]["Linux"]
        node = node_list[0]
        job = "nfs_vaai"
        name = config["PowerStore"]["name"]
        # job_list = ["nvme_vmfs_4k","nvme_vmfs_64k","nvme_vmfs_8k","nvme_vmfs_128k"]
        job_list = [job,job,job,job]
        job_list = list(map(lambda x:name+"_"+x,job_list))
        vdbench = Vdbench()
        df = vdbench.repalce_column_with_value("node",["node1","node2","node3","node4"],[node,node,node,node])
        df = vdbench.repalce_column_with_value("job",["4k","64k","8k","128k"],job_list,df)
        vdbench.run_vdbench("Linux","run",False,df)

    def install_node_exporter(self,jsons,config):
        prefix= jsons["vm"]["nameprefix"]
        sql = "select vm_ip from vm_objs where VM_NAME LIKE '%"+prefix+"%';"
        vms = database.get_data(sql)
        count = 0
        name = config["PowerStore"]["name"]
        user = jsons["vm"]["user"]
        passwd = jsons["vm"]["passwd"]
        for vm in vms:
            NodeHelper.install_exporter_linux(vm[0],user,passwd)
            export_node = name+"_nfs_"+ vm[0]
            NodeHelper.create_pushgateway_cronjob(vm[0],user,passwd,export_node)

    def test_VAAI(self,config,jsons):
        self.init(config,jsons)
        self.init_vcenter_info(jsons)
        #1 create nas server
        with allure.step("create Nas server"):
            self.create_nas(config)
        #2 create interface
        with allure.step("create file interface"):
            self.create_file_interface()
        #3 create SMB server
        with allure.step("create smb server"):
            self.create_smb_server()
        #4 create NFS server
        with allure.step("create nfs server"):
            self.create_nfs_server()
        #5 create filesystem
        with allure.step("create File system"):
            self.create_file_system(config)
        #6 create NFS export
        with allure.step("create nfs export"):
            self.create_nfs_export()
        #7 mount nfs datastore
        with allure.step("mount nfs datastore"):
            self.mount_nfs_datastore(config)
        #8 clone VM
        with allure.step("clone vms"):
            time.sleep(10)
            self.clone_vm(jsons)
        with allure.step("install node exporter"):
            self.install_node_exporter(jsons,config)
        with allure.step("run vdbench"):
            self.run_vdbench(config)

class Test_Clean:
    def setup_class(self):
        self.share = ShareVAAIImpl()
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
            self.esxiExecutor.delete_nfs41_datastore(host,"vaai")

    def delete_file_system(self):
        self.share.delete_file_system_by_rest()

    def delete_nas_server(self):
        self.share.delete_nas_server()

    def delete_pushgateway_job(self,config):
        enable = config["PowerStore"]["vdbench_vm"]["enable"]
        if not enable:
            return
        name = config["PowerStore"]["name"]
        job = name+"_"+"nfs_vaai"
        delete_cmd = "curl -X DELETE http://10.226.112.170:31659/metrics/job/{}".format(job)
        subprocess.run(delete_cmd, shell=True)

    def test_nfs_clean(self,jsons,config):
        self.init_vcenter_info(jsons)
        self.delete_vm(jsons)
        self.delete_ds(config)
        self.delete_file_system()
        self.delete_nas_server()
        self.delete_pushgateway_job(config)





        

