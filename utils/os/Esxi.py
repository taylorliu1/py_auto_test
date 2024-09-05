import re
import ssl
import uuid
from common.databases.database import database
from utils.os import pchelper,tasks
from pyVim import connect
import atexit
from pyVmomi import vim
import paramiko
import time

from utils.wrapper import Go


class EsxiExecutor(object):
    def __init__(self,host,user,password):
        context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        context.verify_mode = ssl.CERT_NONE
        # connect to vCenter or ESXi
        self.si = connect.SmartConnect(
            host=host,
            user=user,
            pwd=password,
            port=443,
            sslContext=context)

        atexit.register(connect.Disconnect, self.si)
        self.content = self.si.RetrieveContent()

    def set_services(self,host_system):
        service_system = host_system.configManager.serviceSystem
        # find SSH service
        ssh_service = [x for x in service_system.serviceInfo.service if x.key == 'TSM-SSH'][0]
        if not ssh_service.running:
            print('Starting SSH ...')
            service_system.Start(ssh_service.key)
            # start and shutdown with host,default is off
            service_system.UpdateServicePolicy(id=ssh_service.key, policy='off')
            print('successfully...')
        else:
            print('Already Started ...')

        return ssh_service

    def execute(self, host, cmd):
        host_system = pchelper.get_obj(self.content,[vim.HostSystem],host)
        self.set_services(host_system)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(host_system.name, username="root", password="#1Danger0us",timeout=30)
            stdin, stdout, stderr = client.exec_command(cmd,timeout=20)
            out = stdout.read().decode().strip()
            error = stderr.read().decode().strip()
            if error != "":
                print("excute {} error on host {}: {}".format(cmd,host,error))
            print("excute {} success on host {}: {}".format(cmd,host,out))
            return out
        except Exception as e:
            print(e)
        finally:
            client.close()

    def get_host_nqn_nvme(self,host):
        cmd = "esxcli nvme info get"
        out = self.execute(host, cmd)
        return out.split(":",1)[1]

    def get_host_iqn_iscsi(self,host):
        adaptor = self.get_iscsi_adaptor(host)[0]
        cmd = "esxcli iscsi adapter get -A {} |grep iqn".format(adaptor)
        out = self.execute(host, cmd)
        iqn = out.split(":",1)[1].strip()
        return iqn

    def get_nvme_adaptor(self,host):
        cmd = "esxcli nvme adapter list| awk 'NR>2 {print $1}'"
        out = self.execute(host, cmd)
        return out.split("\n")

    def get_iscsi_adaptor(self,host):
        cmd = "esxcli iscsi adapter list |grep 'online'| awk '{print $1}'"
        out = self.execute(host, cmd)
        return out.split("\n")
    
    def rescan_nvme_adaptor(self,host):
        adaptors = self.get_nvme_adaptor(host)
        for adaptor in adaptors:
            cmd = "esxcli storage core adapter rescan --adapter={}".format(adaptor)
            self.execute(host, cmd)
            cmd = "vmkfstools -V"
            self.execute(host, cmd)
    
    def rescan_iscsi_adaptor(self,host):
        adaptors = self.get_iscsi_adaptor(host)
        for adaptor in adaptors:
            cmd = "esxcli storage core adapter rescan --adapter={}".format(adaptor)
            self.execute(host, cmd)
            cmd = "vmkfstools -V"
            self.execute(host, cmd)
    
    def rescan_sdc_adaptor(self,host):
        cmd = "esxcli storage core adapter rescan --adapter=vmhba64"
        self.execute(host, cmd)
        cmd = "vmkfstools -V"
        self.execute(host, cmd)

    def get_device_paths(self,host,type):
        device_path_list = []
        if type == "NVME":
            adaptor = self.get_nvme_adaptor(host)[0]
        elif type == "iscsi":
            adaptor = self.get_iscsi_adaptor(host)[0]

        if adaptor == "":
            raise Exception("{} adaptor not found!!!".format(type))
        cmd = 'esxcli storage core path list|grep "State: active" -B 6|grep "Adapter: {}" -B 1|sort -u|grep -v "Adapter"'.format(adaptor)
        out = self.execute(host, cmd)
        outs = out.split("\n")
        pattern = re.compile(r'\(.*?\)')
        for item in outs:
            match = pattern.search(item)
            if match:
                device_id = match.group()[1:-1]
                cmd1 = 'esxcli storage core device list|grep {}|grep " Devfs Path"'.format(device_id)
                out1 = self.execute(host, cmd1)
                device_path = out1.split(":")[1].strip()
                device_path_list.append(device_path)
        return device_path_list
    
    def get_device_paths_sdc(self,host):
        device_path_list = []
        cmd = 'esxcli storage core path list|grep "State: active" -B 6|grep "Adapter: vmhba64" -B 1|sort -u|grep -v "Adapter"'
        out = self.execute(host, cmd)
        outs = out.split("\n")
        pattern = re.compile(r'\(.*?\)')
        for item in outs:
            match = pattern.search(item)
            if match:
                device_id = match.group()[1:-1]
                cmd1 = 'esxcli storage core device list|grep {}|grep " Devfs Path"'.format(device_id)
                out1 = self.execute(host, cmd1)
                device_path = out1.split(":")[1].strip()
                device_path_list.append(device_path)
        return device_path_list

    def get_volume_name_device_path_map_powerflex(self,host,device_path_list):
        volume_name_device_path_map = {}
        sql = "select volume_name,volume_id from sdc_volume_mapping where host = '{}'".format(host)
        query_list = database.get_data(sql)
        for item in query_list:
            volume_name = item[0]
            volume_id = item[1]
            filter_device_path = [device_path for device_path in device_path_list if volume_id in device_path]
            if len(filter_device_path) == 0: continue
            volume_name_device_path_map[filter_device_path[0]]=volume_name
        return volume_name_device_path_map

    def get_volume_name_device_path_map(self,host,device_path_list):
        volume_name_device_path_map = {}
        sql = "select volume_name,volume_wwn from host_volume_mapping where host = '{}'".format(host)
        query_list = database.get_data(sql)
        for item in query_list:
            volume_name = item[0]
            volume_wwn = item[1]
            filter_device_path = [device_path for device_path in device_path_list if volume_wwn[-5:] in device_path]
            if len(filter_device_path) == 0: continue
            volume_name_device_path_map[filter_device_path[0]]=volume_name
        return volume_name_device_path_map

    
    def create_storage(self,host,type="iscsi"):
        device_path_list = []
        if type == "NVME":
            device_path_list = self.get_device_paths(host,type)
        elif type == "iscsi":
            device_path_list = self.get_device_paths(host,type)
        elif type == "sdc":
            device_path_list = self.get_device_paths_sdc(host)
        
        if len(device_path_list) == 0:
            raise Exception("{} device path not found!!!".format(type))
        volume_name_device_path_map = {}
        if type == "sdc":
            volume_name_device_path_map = self.get_volume_name_device_path_map_powerflex(host,device_path_list)
        else:
            volume_name_device_path_map = self.get_volume_name_device_path_map(host,device_path_list)
        print (volume_name_device_path_map)
        for device_path,volume_name in volume_name_device_path_map.items():
            volume_count_cmd = '''vim-cmd hostsvc/datastore/listsummary | grep 'name = '  | awk -F'"' '{print $2}' | grep -c %s''' % volume_name
            volume_count = self.execute(host,volume_count_cmd)
            if int(volume_count) == 0:
                name = "datastore_"+ volume_name
                get_end_sector_cmd = '''eval expr $(partedUtil getptbl %s | tail -1 | awk '{print $NF " - 34"}')''' % (device_path)
                print (get_end_sector_cmd)
                end_sector = self.execute(host, get_end_sector_cmd)
                print ("end_sector : %s" % (end_sector))
                create_partition_cmd = '/sbin/partedUtil "setptbl" "{}" "gpt" "1 2048 {} AA31E02A400F11DB9590000C2911D1B8 0"'.format(device_path,end_sector)
                print (create_partition_cmd)
                self.execute(host, create_partition_cmd)
                create_datastore_cmd = "vmkfstools -C vmfs6 -S {} {}:1".format(name,device_path)
                print (create_datastore_cmd)
                self.execute(host, create_datastore_cmd)
                sql = "insert into block_datastore_objs (Esxi_host, VMFS_datastore) values ( '" + host + "','" + name + "');"
                database.insert_data(sql)
    
    def delete_nvme_datastore(self,host):
        nvme_datastores_cmd = "esxcli storage filesystem list | grep nvme | awk '{print $2}'"
        out =  self.execute(host,nvme_datastores_cmd)
        outs = out.split("\n")
        for datastore in outs:
            delete_datastore_cmd = "vim-cmd hostsvc/datastore/remove {}".format(datastore)
            self.execute(host,delete_datastore_cmd)
            database.delete_data("delete from block_datastore_objs where VMFS_datastore='{0}';".format(datastore))


    def discover_nvme_fabrics(self,host):
        nvme_adaptor = self.get_nvme_adaptor(host)
        for adaptor in nvme_adaptor:
            cmd1 = "esxcli nvme fabrics discover  -a {}  -i 192.168.41.15 -p 8009 -r -c".format(adaptor)
            self.execute(host, cmd1)
            cmd2 = "esxcli nvme fabrics discover  -a {}  -i 192.168.49.15 -p 8009 -r -c".format(adaptor)
            self.execute(host, cmd2)
    
    def delete_vm_by_name_prefix(self,prefix):
        vms = pchelper.get_all_obj(self.content,[vim.VirtualMachine])
        for vm in vms:
            if prefix in vm.name:
                if format(vm.runtime.powerState) == "poweredOn":
                     print("Attempting to power off {0}".format(vm.name))
                     TASK = vm.PowerOffVM_Task()
                     tasks.wait_for_tasks(self.si, [TASK])
                     print("{0}".format(TASK.info.state))
                print("Destroying VM {} from vSphere.".format(vm.name))
                TASK = vm.Destroy_Task()
                tasks.wait_for_tasks(self.si, [TASK])
                print("Done.")
    
    def delete_nfs_datastore(self,host):
        nfs_datastores_cmd = "esxcli storage filesystem list | grep NAS |grep true| awk '{print $2}'"
        out =  self.execute(host,nfs_datastores_cmd)
        if out is None or out =="" : return
        outs = out.split("\n")
        for datastore in outs:
            delete_datastore_cmd = "esxcli storage nfs41 remove -v {}".format(datastore)
            self.execute(host,delete_datastore_cmd)
            database.delete_data("delete from datastore_objs where NFS_datastore='{0}';".format(datastore))

    def delete_nfs41_datastore(self,host,prefix):
        nfs_datastores_cmd = "esxcli storage nfs41 list | grep '%s' |grep true| awk '{print $1}'" % prefix
        out =  self.execute(host,nfs_datastores_cmd)
        if out is None or out =="" : return
        outs = out.split("\n")
        for datastore in outs:
            delete_datastore_cmd = "esxcli storage nfs41 remove -v {}".format(datastore)
            self.execute(host,delete_datastore_cmd)
            database.delete_data("delete from datastore_objs where NFS_datastore='{0}';".format(datastore))

    def mount_nfs_datastore(self,esxi_hosts,prefix):
        # get mount path
        # volume_list = list()
        nfs_list = database.get_data("select nfspath from filesystem_objs;")
        print(nfs_list)
        number_of_nfs_export = len(nfs_list)
        # mount nfs datastore to esxi host
        for i in range(number_of_nfs_export):
            # volume_name = prefix + "_" + database.generate_random_str(6)
            # volume_list.append(volume_name)
            # index = i % len(esxi_hosts)
            nfs_export_info = nfs_list[i][0].split(":")
            self.mount_async(esxi_hosts, nfs_export_info)

    def mount_async(self, esxi_hosts, nfs_export_info):
        cmd = "esxcli storage nfs41 add --hosts={0} --share={1} --volume-name={2}".format(nfs_export_info[0],
                                                                                              nfs_export_info[1],
                                                                                              nfs_export_info[1][1:])
        print (cmd)
            # cmd = "esxcli storage nfs41 list"
        for host in esxi_hosts:
            sql = "insert into datastore_objs (Esxi_host, NFS_datastore) values ( '" + host + "','" + nfs_export_info[1][1:] + "');"            
            self.execute(host,cmd)
            database.insert_data(sql)

    def delete_iscsi_datastore(self,host):
        nvme_datastores_cmd = "esxcli storage filesystem list | grep iscsi | awk '{print $2}'"
        out =  self.execute(host,nvme_datastores_cmd)
        outs = out.split("\n")
        for datastore in outs:
            delete_datastore_cmd = "vim-cmd hostsvc/datastore/remove {}".format(datastore)
            self.execute(host,delete_datastore_cmd)
            database.delete_data("delete from block_datastore_objs where VMFS_datastore='{0}';".format(datastore))


    def delete_block_datastore(self,host):
        datastores = database.get_data("select VMFS_datastore from block_datastore_objs;")
        print(datastores)
        for datastore in datastores:
            delete_datastore_cmd = "vim-cmd hostsvc/datastore/remove {}".format(datastore[0])
            self.execute(host,delete_datastore_cmd)
            database.delete_data("delete from block_datastore_objs where VMFS_datastore='{0}';".format(datastore[0]))