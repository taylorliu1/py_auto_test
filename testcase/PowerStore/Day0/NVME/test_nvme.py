import json
from PowerStore.NVME.volumeNVMeImpl import VolumeNVMeImpl
import os
from common.databases.database import database
from common.monitor.node_exporter_deployment import NodeHelper
from prime.swagger_client.rest import ApiException
from utils.os.Esxi import EsxiExecutor
from utils.os.Linux import Executor
from utils.vsphere.VMUtil import VM
import allure
from utils.workload.vdbench.vdbench import Vdbench
class Test_Setup:
    @allure.title("test NVME day0")
    @allure.description("test NVME day0 description")
    def setup_class(self):
        print("create tables if not exist")
        self.nvme = VolumeNVMeImpl()
        database.init_DB()
        self.vm = VM()
        
    
    def teardown_class(self):
        print("teardown test case")


    def init(self, config,jsons):
        print("init nvme dabase")
        trident_ip = config['PowerStore']['nvme']['url']
        user = config['PowerStore']['nvme']['user']
        pwd = config['PowerStore']['nvme']['pwd']
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

    def create_volume(self,config):
        hosts = config["PowerStore"]["esxi_hosts"]
        num = config["PowerStore"]["volume"]["num"]
        size = config["PowerStore"]["volume"]["size"]
        self.nvme.create_vloume(num,hosts,size)

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
            NodeHelper.install_exporter_linux(vm[0],"root","Admin@123")
            # check_url = "http://{0}:{1}/metrics".format(vm[0],9100)
            # NodeExporter.register_to_consul("10.226.112.81","node_exporter","linux"+"".join(vm[0].split('.')),9100,check_url)
            # excutor = Executor("10.226.69.47", "root", "#1Danger0us")
            # ret = excutor.execute("curl {0}".format(check_url))
            # result =re.search(r'promhttp_metric_handler_requests_total{code="200"} (\d+)',ret)
            # assert int(result.group(1)) >= 0
            export_node = name+"_nvme_"+ vm[0]
            NodeHelper.create_pushgateway_cronjob(vm[0],"root","Admin@123",export_node)

    
    def run_vdbench(self,config):
        enable = config["PowerStore"]["vdbench_vm"]["enable"]
        if not enable:
            return
        node_list = config["PowerStore"]["vdbench_vm"]["Linux"]
        node = node_list[0]
        job = "nvme_vmfs"
        name = config["PowerStore"]["name"]
        # job_list = ["nvme_vmfs_4k","nvme_vmfs_64k","nvme_vmfs_8k","nvme_vmfs_128k"]
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
                excutor = Executor(vm_ip, "root","Admin@123")
                excutor.create_vdisk()

    def test_nvme(self,jsons,config):
        self.init(config,jsons)
        self.init_vcenter_info(jsons)
        with allure.step("create nvme host"):  
            self.create_host(config,jsons)
        with allure.step("create vnme volume"):
            self.create_volume(config)
        with allure.step("create vmfs datastore"):
            self.create_datastore(config)
        with allure.step("clone vms"):
            self.clone_vms(jsons)
        # with allure.step("install node exporter"):
        #     self.install_node_exporter(jsons,config)
        with allure.step("create vdisk and attach to vm"):
            self.create_vd_attach_vm(config)
        # with allure.step("run vdbench"):
        #     self.run_vdbench(config)


  
class Test_Clean:
    def setup_class(self):
        self.nvme = VolumeNVMeImpl()
        # database.init_DB()
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
    #     print("init nvme dabase")
    #     trident_ip = config['PowerStore']['taylor']['url']
    #     user = config['PowerStore']['taylor']['user']
    #     pwd = config['PowerStore']['taylor']['pwd']
    #     sql = "insert into trident_objs (ip, user, password) values ( '"+trident_ip+"','"+user+"','"+pwd+"');"
    #     try:
    #         database.insert_data(sql)
    #     except Exception as e:
    #         print (e)
    #     print("init vsphere dabase")
        self.init_vcenter_info(jsons)

    def delete_vm(self,jsons):
        prefix= jsons["vm"]["nameprefix"]
        self.vm.delete_vm(prefix)

    def delete_ds(self, config):
        hosts = config["PowerStore"]["esxi_hosts"]
        self.esxiExecutor.delete_nvme_datastore(hosts[0])

    def unmap_host(self,config):
        hosts = config["PowerStore"]["esxi_hosts"]
        for host in hosts:
            self.nvme.unmap_host_by_name(host)

    def delete_volume(self):
        self.nvme.delete_volume()

    def delete_host(self, config):
        hosts = config["PowerStore"]["esxi_hosts"]
        for host in hosts:
            self.nvme.delete_host_by_name(host)
    
    def rescan_datastore(self, config):
        hosts = config["PowerStore"]["esxi_hosts"]
        for host in hosts:
            self.esxiExecutor.rescan_nvme_adaptor(host)

    def test_nvme_clean(self,jsons,config):
        self.init(config,jsons)
        self.init_vcenter_info(jsons)
        self.delete_vm(jsons)
        self.delete_ds(config)
        self.unmap_host(config)
        self.delete_volume()
        self.delete_host(config)
        self.rescan_datastore(config)



    





        

