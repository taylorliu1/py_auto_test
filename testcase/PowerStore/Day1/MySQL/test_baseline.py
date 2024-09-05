import allure
from common.databases.database import database
import os
from utils.os.Esxi import EsxiExecutor
from PowerStore.NVME.volumeNVMeImpl import VolumeNVMeImpl
from prime.swagger_client.rest import ApiException
import json
from utils.os.Linux import Executor
from utils.vsphere.VMUtil import VM

class Test_Setup:
    @allure.title("test NVME MySQL baseline")
    @allure.description("test NVME MySQL baseline description")
    def setup_class(self):
        print("create tables if not exist")
        database.init_DB()
        self.nvme = VolumeNVMeImpl()
        self.vm = VM()

    def teardown_class(self):
        print("teardown test case")

    def init(self, config,jsons):
        print("init baseline dabase")
        trident_ip = config['PowerStore']['baseline']['url']
        user = config['PowerStore']['baseline']['user']
        pwd = config['PowerStore']['baseline']['pwd']
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

    def create_volume(self,config):
        hosts = config["PowerStore"]["esxi_hosts"]
        num = config["PowerStore"]["volume"]["num"]
        size = config["PowerStore"]["volume"]["size"]
        self.nvme.create_vloume(num,hosts,size)

    def create_host(self,config,jsons):      
        hosts = config["PowerStore"]["esxi_hosts"]
        vc = jsons["vsphere"]["vcenter"]
        user = jsons["vsphere"]["user"]
        password = jsons["vsphere"]["password"]
        for host in hosts:
            try:
                self.nvme.create_nvme_host_by_name(vc,user,password,host)
            except ApiException as e:
                js=json.loads(e.body)
                msg = js['messages'][0]['message_l10n']
                if "One of the provided port names is already registered" in msg:
                    continue
                else:
                    raise e

    def create_datastore(self,config):
        hosts = config["PowerStore"]["esxi_hosts"]
        self.esxiExecutor.create_storage(hosts[0],type="NVME")
        for host in hosts:
            # self.esxiExecutor.discover_nvme_fabrics(host)
            self.esxiExecutor.rescan_nvme_adaptor(host)

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
        print("start cloning vms...")
        self.vm.clone_vm_from_range(ip_range,base,os,net,custmask,custgw,prefix,[datastore])
        sql = "select count(*) from vm_objs;"
        count = database.get_data(sql)[0][0]
        assert count != 0
        print("clone vms finished!")

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
                excutor.create_vdisk_nvme()