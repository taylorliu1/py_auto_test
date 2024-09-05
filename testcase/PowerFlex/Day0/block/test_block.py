import re
from PowerFlex.block.blockImpl import BlockImpl
import os
import json
from common.databases.database import database
from common.monitor.node_exporter_deployment import NodeHelper
import pytest
from utils.os.Esxi import EsxiExecutor
from utils.vsphere.VMUtil import VM
from prime.swagger_client.rest import ApiException
from utils.workload.vdbench.vdbench import Vdbench
import time
import allure
class Test_Setup:
    @allure.title("test block sdc day0")
    @allure.description("test block sdc day0 description")
    def setup_class(self):
        print("create tables if not exist")   
        database.init_DB()
        self.vm = VM()


    def teardown_class(self):
        print("teardown test case")


    def init(self, config,jsons):
        print("init block dabase")
        pflex_ip = config['PowerFlex']['block']['url']
        user = config['PowerFlex']['block']['user']
        pwd = config['PowerFlex']['block']['pwd']
        sql = "insert into pflex_objs (ip, user, password) values ( '"+pflex_ip+"','"+user+"','"+pwd+"');"
        try:
            database.insert_data(sql)
        except Exception as e:
            print (e)
        self.block = BlockImpl()
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


    def create_volume(self,config):
        hosts = config["PowerFlex"]["esxi_hosts"]
        num = config["PowerFlex"]["volume"]["num"]
        size = config["PowerFlex"]["volume"]["size"]
        ips = config["PowerFlex"]["volume"]["ips"]
        storagePool = config["PowerFlex"]["volume"]["storagePool"]
        self.block.create_vloume(num,hosts,ips,size,storagePool)

    def create_datastore(self,config):
        hosts = config["PowerFlex"]["esxi_hosts"]
        for host in hosts:
            self.esxiExecutor.rescan_sdc_adaptor(host)
            self.esxiExecutor.create_storage(host, type="sdc")

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
        name = config["PowerFlex"]["name"]
        for vm in vms:
            NodeHelper.install_exporter_linux(vm[0],"root","#1Danger0us")
            export_node = name+"_sdc_"+ vm[0]
            NodeHelper.create_pushgateway_cronjob(vm[0],"root","#1Danger0us",export_node)

    def run_vdbench(self,config):
        enable = config["PowerFlex"]["vdbench_vm"]["enable"]
        if not enable:
            return
        node_list = config["PowerFlex"]["vdbench_vm"]["Linux"]
        node = node_list[0]
        job = "sdc_vmfs"
        name = config["PowerFlex"]["name"]
        job_list = [job,job,job,job]
        job_list = list(map(lambda x:name+"_"+x,job_list))
        vdbench = Vdbench()
        df = vdbench.repalce_column_with_value("node",["node1","node2","node3","node4"],[node,node,node,node])
        df = vdbench.repalce_column_with_value("job",["4k","64k","8k","128k"],job_list,df)
        vdbench.run_vdbench("Linux","run",False,df)

    def test_block(self,jsons,config):
        self.init(config,jsons)
        self.init_vcenter_info(jsons)
        with allure.step("create sdc volume"):
            self.create_volume(config)
        with allure.step("create vmfs datastore"):
            self.create_datastore(config)
        with allure.step("clone vms"):
            time.sleep(30)
            self.clone_vms(jsons)
        with allure.step("install node exporter"):
            self.install_node_exporter(jsons,config)
        with allure.step("run vdbench"):
            self.run_vdbench(config)



class Test_Clean:
    def setup_class(self):
        self.block = BlockImpl()
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
        hosts = config["PowerFlex"]["esxi_hosts"]
        self.esxiExecutor.delete_block_datastore(hosts[0])

    def unmap_host(self,config):
        hosts = config["PowerFlex"]["esxi_hosts"]
        for host in hosts:
            self.block.remove_mapped_sdc_by_host(host)

    def delete_volume(self):
        self.block.delete_volume()


    def rescan_datastore(self, config):
        hosts = config["PowerFlex"]["esxi_hosts"]
        for host in hosts:
            self.esxiExecutor.rescan_sdc_adaptor(host)

    def test_block_clean(self,jsons,config):
        self.init(config,jsons)
        self.init_vcenter_info(jsons)
        self.delete_vm(jsons)
        self.delete_ds(config)
        self.unmap_host(config)
        self.delete_volume()
        self.rescan_datastore(config)
