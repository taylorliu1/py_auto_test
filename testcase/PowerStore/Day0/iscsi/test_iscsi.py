import re
from PowerStore.iscsi.iscsiImpl import IscsiImpl
import os
import json
from common.databases.database import database
from common.monitor.node_exporter_deployment import NodeHelper
from utils.os.Esxi import EsxiExecutor
from utils.os.Linux import Executor
from utils.vsphere.VMUtil import VM
from prime.swagger_client.rest import ApiException
from utils.workload.vdbench.vdbench import Vdbench
import time
import allure
class Test_Setup:
    @allure.title("test iscsi day0")
    @allure.description("test iscsi day0 description")
    def setup_class(self):
        print("create tables if not exist")
        self.iscsi = IscsiImpl()
        database.init_DB()
        self.vm = VM()


    def teardown_class(self):
        print("teardown test case")


    def init(self, config,jsons):
        print("init iscsi dabase")
        trident_ip = config['PowerStore']['iscsi']['url']
        user = config['PowerStore']['iscsi']['user']
        pwd = config['PowerStore']['iscsi']['pwd']
        sql = "insert into trident_objs (ip, user, password) values ( '"+trident_ip+"','"+user+"','"+pwd+"');"
        try:
            database.insert_data(sql)
        except Exception as e:
            print(e)
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


    def create_host(self,config,jsons):      
        hosts = config["PowerStore"]["esxi_hosts"]
        vc = jsons["vsphere"]["vcenter"]
        user = jsons["vsphere"]["user"]
        password = jsons["vsphere"]["password"]
        for host in hosts:
            try:
                self.iscsi.create_iscsi_host_by_name(vc,user,password,host)
            except ApiException as e:
                js=json.loads(e.body)
                msg = js['messages'][0]['message_l10n']
                if "One of the provided port names is already registered" in msg:
                    continue
                else:
                    raise e

    def create_volume(self,config):
        hosts = config["PowerStore"]["esxi_hosts"]
        num = config["PowerStore"]["volume"]["num"]
        size = config["PowerStore"]["volume"]["size"]
        self.iscsi.create_vloume(num,hosts,size)

    def create_datastore(self,config):
        hosts = config["PowerStore"]["esxi_hosts"]
        for host in hosts:
            self.esxiExecutor.rescan_iscsi_adaptor(host)
            self.esxiExecutor.create_storage(host)

    def clone_vms(self,jsons):
        ip_range = jsons["ip"]["ens192"]["range"]
        base = jsons["vm"]["base"]
        os = jsons["vm"]["os"]
        net = jsons["ip"]["ens192"]["net"]
        custmask = jsons["ip"]["ens192"]["mask"]
        custgw = jsons["ip"]["ens192"]["gateway"]
        prefix= jsons["vm"]["nameprefix"]
        # Get datastore info
        datastore_list = database.get_data("select VMFS_datastore from block_datastore_objs;")
        print("start cloning vms...")
        self.vm.clone_vm_from_range(ip_range,base,os,net,custmask,custgw,prefix,datastore_list)
        sql = "select count(*) from vm_objs;"
        count = database.get_data(sql)[0][0]
        assert count != 0
        print("clone vms finished!")


    def install_node_exporter(self,jsons,config):
        prefix= jsons["vm"]["nameprefix"]
        sql = "select vm_ip from vm_objs where VM_NAME LIKE '%"+prefix+"%';"
        vms = database.get_data(sql)
        count = 0
        name = config["PowerStore"]["name"]
        for vm in vms:
            NodeHelper.install_exporter_linux(vm[0],"root","#1Danger0us")
            export_node = name+"_iscsi_"+ vm[0]
            NodeHelper.create_pushgateway_cronjob(vm[0],"root","#1Danger0us",export_node)

    def run_vdbench(self,config):
        enable = config["PowerStore"]["vdbench_vm"]["enable"]
        if not enable:
            return
        node_list = config["PowerStore"]["vdbench_vm"]["Linux"]
        node = node_list[0]
        job = "iscsi_vmfs"
        name = config["PowerStore"]["name"]
        job_list = [job,job,job,job]
        job_list = list(map(lambda x:name+"_"+x,job_list))
        vdbench = Vdbench()
        df = vdbench.repalce_column_with_value("node",["node1","node2","node3","node4"],[node,node,node,node])
        df = vdbench.repalce_column_with_value("job",["4k","64k","8k","128k"],job_list,df)
        vdbench.run_vdbench("Linux","run",False,df)

    def create_vd_attach_vm(self,config):
        vd_num = config["PowerStore"]["vdisk"]["num"]
        size = config["PowerStore"]["vdisk"]["size"]
        raw = config["PowerStore"]["vdisk"]["raw"]
        sql = "select vm_name,vm_ip from vm_objs;"
        vms = database.get_data(sql)
        vm_names = [vm[0] for vm in vms]
        vm_ips = [vm[1] for vm in vms]
        for vm_name in vm_names:
            self.vm.create_vd_attach_vm(vm_name,vd_num,size)
        if not raw:
            for vm_ip in vm_ips:
                excutor = Executor(vm_ip, "root","#1Danger0us")
                excutor.create_vdisk()

    def test_iscsi(self,jsons,config):
        self.init(config,jsons)
        self.init_vcenter_info(jsons)
        with allure.step("create iscsi host"):  
            self.create_host(config,jsons)
        with allure.step("create iscsi volume"):
            self.create_volume(config)
        with allure.step("create vmfs datastore"):
            self.create_datastore(config)
        with allure.step("clone vms"):
            time.sleep(10)
            self.clone_vms(jsons)
        # with allure.step("install node exporter"):
        #     self.install_node_exporter(jsons,config)
        with allure.step("create vdisk and attach to vm"):
            self.create_vd_attach_vm(config)
        # with allure.step("run vdbench"):
        #     self.run_vdbench(config)



class Test_Clean:
    def setup_class(self):
        self.iscsi = IscsiImpl()
        self.vm = VM()

    def init_vcenter_info(self,jsons):
        os.environ["GOVC_URL"] = jsons["vsphere"]["vcenter"]
        os.environ["GOVC_USERNAME"] = jsons["vsphere"]["user"]
        os.environ["GOVC_PASSWORD"] = jsons["vsphere"]["password"]
        os.environ["GOVC_INSECURE"] = jsons["vsphere"]["insecure"]
        os.environ["GOVC_DATACENTER"] = jsons["vsphere"]["datacenter"]
        os.environ["GOVC_RESOURCE_POOL"] = jsons["vsphere"]["respool"]
        self.esxiExecutor = EsxiExecutor(jsons["vsphere"]["vcenter"],jsons["vsphere"]["user"],jsons["vsphere"]["password"])

    def init(self, config,jsons):
        self.init_vcenter_info(jsons)

    def delete_vm(self,jsons):
        prefix= jsons["vm"]["nameprefix"]
        self.vm.delete_vm(prefix)

    def delete_ds(self, config):
        hosts = config["PowerStore"]["esxi_hosts"]
        self.esxiExecutor.delete_block_datastore(hosts[0])

    def unmap_host(self,config):
        hosts = config["PowerStore"]["esxi_hosts"]
        for host in hosts:
            self.iscsi.unmap_host_by_name(host)

    def delete_volume(self):
        self.iscsi.delete_volume()

    def delete_host(self, config):
        hosts = config["PowerStore"]["esxi_hosts"]
        for host in hosts:
            self.iscsi.delete_host_by_name(host)

    def rescan_datastore(self, config):
        hosts = config["PowerStore"]["esxi_hosts"]
        for host in hosts:
            self.esxiExecutor.rescan_iscsi_adaptor(host)

    def test_iscsi_clean(self,jsons,config):
        self.init(config,jsons)
        self.init_vcenter_info(jsons)
        self.delete_vm(jsons)
        self.delete_ds(config)
        self.unmap_host(config)
        self.delete_volume()
        self.delete_host(config)
        self.rescan_datastore(config)