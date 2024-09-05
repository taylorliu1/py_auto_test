from concurrent.futures import ThreadPoolExecutor
import logging
import os
import socket
import struct
import subprocess
from threading import Thread
from time import sleep
from utils.vsphere.IPy import IP
from common.databases.database import database
#from macpath import join

# from IPy import IP
from common.databases.database import database
from common.monitor.node_exporter_deployment import NodeHelper

OS_INFO = {
        "Linux":  {
            "STOS": "STOS",
            "RHAT": "RHAT",
            "SLES": "SLES",
        },
        "Windows": {
            "TWin10":   "TWin10",
        }
    }

class VM(object):

    def async_call(fun):
        def wrapper(*args, **kwargs):
            t = Thread(target=fun, args=args, kwargs=kwargs)
            # t.setDaemon(True)
            t.start()
            t.join()

        return wrapper

    def check_platform(self,os):
        linux = OS_INFO['Linux'].keys()
        for key in linux:
            if key == os:
                return "Linux"
        windows = OS_INFO['Windows'].keys()
        for key in windows:
            if key == os:
                return "Windows"
        return None


    def create_names(self,vm_num,prefix):
        names = list()
        
        for i in range(vm_num):
            names.append(f"{prefix}{i + 1}")
        # with open(r'C:\Users\test\code\AutoTest\config\config.txt', 'w') as f:
        #     name_list = json.dumps(names)
        #     f.write(name_list)
        # print(names)
        return names

    def CreateIP(self,ips,num):
        """https://wenku.baidu.com/view/91b14b850329bd64783e0912a216147917117edb.html
        """
        ips = IP(ips)
        ip_min = ips[0]
        ip_max = ips[255]
        ip_list = list()
        for ip in ips:
            # print(type(ip))
            if num == 0:
                return ip_list
            else:
                if ip.int() != ip_min.int() and ip.int() != ip_max.int():
                    ip_list.append(str(ip))
                    num = num - 1
                else:
                    continue

    def ip2int(self,addr):
        return struct.unpack("!I", socket.inet_aton(addr))[0]


    def int2ip(self,addr):
        return socket.inet_ntoa(struct.pack("!I", addr))

    
    def clone_vm_from_range(self,ip_range,base,os,net,custmask,custgw,prefix,ds):
        type = self.check_platform(os)
        if not type:
            logging.error(f"Fail to clone vm {os} not support!")
            return
        ip_start = ip_range.split("-")[0]
        ip_end = ip_range.split("-")[1]
        ip_start_int = self.ip2int(ip_start)
        ip_end_int = self.ip2int(ip_end)
        count = 1
        tasks = []
        tmp=0
        for i in range(ip_start_int,ip_end_int+1):
            tmp = tmp + 1
            if (count % 10) == 0:
                sleep(10)
            ip = self.int2ip(i)
            ip_tmp = ip.split(".")
            ip_name = ip_tmp[2] + "." + ip_tmp[3]
            vm_name = prefix+"_"+base+ "_" + ip_name
            thread=Thread(target = self.clone_vm,args=(vm_name,ip,base,type,net,custmask,custgw,None))
            if len(ds) !=0:
                index = tmp % len(ds)
                thread=Thread(target = self.clone_vm,args=(vm_name,ip,base,type,net,custmask,custgw,ds[index][0]))
                
                
            thread.start()
            tasks.append(thread)
        for t in tasks:
            t.join()
        sleep(120)

    def clone_vm_on_vmfs(self,ip_range,winbase,cenbase,net,custmask,custgw,prefix,ds):
        type = ""
        ip_start = ip_range.split("-")[0]
        ip_end = ip_range.split("-")[1]
        ip_start_int = self.ip2int(ip_start)
        ip_end_int = self.ip2int(ip_end)
        count = 1
        tasks = []
        tmp=0
        for i in range(ip_start_int,ip_end_int+1):
            if i%2 == 0:
                type = "Windows"
                base = winbase
            else:
                type = "Linux"
                base = cenbase
            tmp = tmp + 1
            if (count % 10) == 0:
                sleep(10)
            ip = self.int2ip(i)
            ip_tmp = ip.split(".")
            ip_name = ip_tmp[2] + "." + ip_tmp[3]
            vm_name = prefix+"_"+base+ "_" + ip_name
            thread=Thread(target = self.clone_vm,args=(vm_name,ip,base,type,net,custmask,custgw,ds))                
            thread.start()
            tasks.append(thread)
        for t in tasks:
            t.join()
        sleep(120)

    def run_cmd(self, command, capture_output=True):
        logging.info(f"Run command {command}")
        # print(command)
        ret = subprocess.run(command, shell=True, capture_output=capture_output)
        msg = f"Fail to execute {command}"
        if capture_output:
            if ret.returncode != 0:
                stderr = ret.stderr.decode()
                if stderr != "":
                    return stderr
                else:
                    return msg
        else:
            if ret.returncode != 0:
                return msg
        # stdout = ret.stdout.decode()
        return None

    def clone_vm(self, name,ip,base,type,net,custmask,custgw,ds):
        cmd_str = "./tools/govc vm.clone -net={0} -debug=true -custip={1} -custmask={2} -custgw={3} -customization={4} -vm=/{5}/vm/{6} {7} > /tmp/{8}.log" .format(net, ip, custmask,custgw,type,os.environ["GOVC_DATACENTER"],base,name,name)
        if ds:
            cmd_str = "./tools/govc vm.clone -ds={0} -net={1} -debug=true -custip={2} -custmask={3} -custgw={4} -customization={5} -vm=/{6}/vm/{7} {8} > /tmp/{9}.log" .format(ds,net, ip, custmask,custgw,type,os.environ["GOVC_DATACENTER"],base,name,name)
        
        sql = "insert into vm_objs (vm_name, vm_ip, type,datastore) values ( '" + name + "','" + ip + "','" + type + "','" + ds +"');"
        ret = self.run_cmd(cmd_str, True)
        if ret:
            logging.error(f"Fail to clone vm {name} due to {ret}")
        else:
            database.insert_data(sql)
            logging.info(f"Successfully clone VM {name}")

    def clone_vm1(self, name, ip, datastore,vm_base):
        """
        command = [GOVC_EXE, "vm.clone", "-vm", base, name, "-net", "25g_1", "-debug", "true", "-custip","172.100.70.15", "-custmask", "255.255.0.0", "-custgw", "172.100.0.1", "-customization", "Windows"]
        command = [GOVC_EXE, "vm.clone", "-vm=", base, base, "-net=","25g_1", "-debug=", "true", "-custip=", "172.100.70.16", "-custmask=", "255.255.0.0", "-custgw=", "172.100.0.1", "-customizatio=", "Windows"]
        cmd_list = [GOVC_EXE, "vm.clone"]
        cmd_str = "{0} vm.clone -net=25g_1 -debug=true -custip={1} -custmask=255.255.0.0 -custgw=172.100.0.1 -customization=Linux -vm={2} {3}" .format(GOVC_EXE, ip, base, name)
        cmd_str = "{0} vm.clone -net=25g_1 -debug=true -net.address=={1} -net.mask=255.255.0.0 -net.gw=172.100.0.1 -customization=Windows -ds={2} -vm={3} {4}" .format(GOVC_EXE, ip, datastore, base, name)
        :param name:
        :param ip:
        :param datastore:
        :return:
        """

        cmd_str = "./tools/govc vm.clone -ds={0} -vm={1} {2}".format(datastore, vm_base, name)
        # conn = init_db("db_1")
        # conn.exec(create_vm_obj)
        # sql = "insert into vm_objs (vm_name, vm_ip) values ( '" + name + "','" + ip + "');"
        ret = self.run_cmd(cmd_str, True)
        if ret:
            logging.error(f"Fail to clone vm {name} due to {ret}")
        else:
            logging.info(f"Successfully clone VM {name}")

    def clone_vm_on_default_datastore(self, name, ip, vm_base):
        cmd_str = "./tools/govc vm.clone -net=25g_1 -debug=true -custip={0} -custmask=255.255.128.0 -custgw=172.16.0.1 " \
                  "-customization=Linux -vm={1} {2}".format(ip, vm_base, name)
        ret = self.run_cmd(cmd_str, True)
        print(cmd_str)
        if ret:
            logging.error(f"Fail to clone vm {name} due to {ret}")
        else:
            logging.info(f"Successfully clone VM {name}")
        # cmd_clone = "./tools/govc vm.clone -on=false -vm={0} {1}".format(vm_base, name)
        # ret = self.run_cmd(cmd_clone, True)
        # print(cmd_clone)
        # if ret:
        #     logging.error(f"Fail to clone vm {name} due to {ret}")
        # else:
        #     logging.info(f"Successfully clone VM {name}")
        # cmd_customize = "./tools/govc vm.customize -vm={0} -gateway=172.100.0.1 -ip={1} -netmask=255.255.0.0" .format(name, ip)
        # ret = self.run_cmd(cmd_customize, True)
        # print(cmd_customize)
        # if ret:
        #     logging.error(f"Fail to customize vm {name} due to {ret}")
        # else:
        #     logging.info(f"Successfully customize VM {name}")
        # cmd_power_on = "./tools/govc vm.power -on {0}" .format(name)
        # ret = self.run_cmd(cmd_power_on, True)
        # print(cmd_power_on)
        # if ret:
        #     logging.error(f"Fail to power on vm {name} due to {ret}")
        # else:
        #     logging.info(f"Successfully power on VM {name}")
    
    def create_vm_snapshot(self):
        new_name = "snapshot_"+database.generate_random_str(5)
        sql = "select vm_name from vm_objs;"
        lst = database.get_data(sql)
        for vm in lst:
            cmd_str = "{0} snapshot.create -vm {1} {2}".format("./tools/govc",vm[0], new_name)
            ret = self.run_cmd(cmd_str, True)
            if ret:
                logging.error(f"Fail to create snapshot of vm {vm[0]} due to {ret}")
            else:
                logging.info(f"Successfully create snapshot of VM {vm[0]}")

    def delete_vm_snapshot(self):
        sql = "select vm_name from vm_objs;"
        lst = database.get_data(sql)
        for vm in lst:
            cmd_str = "{0} snapshot.remove -vm {1} *".format("./tools/govc", vm[0])
            ret = self.run_cmd(cmd_str, True)
            if ret:
                logging.error(f"Fail to delete snapshot of vm {vm[0]} due to {ret}")
            else:
                logging.info(f"Successfully delete snapshot of vm {vm[0]}")

    def delete_vm(self,prefix):
        sql = "select vm_name,vm_ip,type from vm_objs where vm_name like '%"+prefix+"%';"
        lst = database.get_data(sql)
        with ThreadPoolExecutor(max_workers=10) as executor:
            for vm in lst:
                executor.submit(self.async_delete_vm,vm)

    def async_delete_vm(self, vm):
        vm_ip = vm[1]
        type = vm[2]
        service_id = type.lower() + "".join(vm_ip.split('.'))
        cmd_str = "./tools/govc vm.destroy -debug=true /{0}/vm/{1}  > /tmp/{2}.log".format(os.environ["GOVC_DATACENTER"], vm[0],vm[0])
        ret = self.run_cmd(cmd_str, True)
        if ret:
            logging.error(f"Fail to delete vm {vm[0]} due to {ret}")
        else:
            logging.info(f"Successfully delete vm {vm[0]}")                
                # NodeExporter.deregister_to_consul(service_id)
            database.delete_data("delete from vm_objs where vm_name='{0}';".format(vm[0]))
    

    def create_vd_attach_vm(self, vm_name,vd_number,vd_size,type="block"):
        if vd_number == 0:
            return
        sql = "select datastore from vm_objs where VM_NAME = '%s';" % (vm_name)
        lst = database.get_data(sql)
        vm_ds = lst[0][0]
        sql2 = "select VMFS_datastore,height from block_datastore_objs where VMFS_datastore != '%s' order by height limit %d;" % (vm_ds,vd_number)
        if type=="file":
            sql2 = "select NFS_datastore,height from datastore_objs where NFS_datastore != '%s' order by height limit %d;" % (vm_ds,vd_number)      
        lst2 = database.get_data(sql2)
        i = 1
        for ds in lst2:
            i += 1
            cmd_str = "./tools/govc vm.disk.create -ds={0} -vm {1} -name {2}/disk{3} -size {4}G ".format(ds[0],vm_name,vm_name,i,vd_size)
            ret = self.run_cmd(cmd_str, True)
            if ret:
                print("Fail to attach vm {0} due to {1}.".format(vm_name,ret))
                # logging.error(f"Fail to attach vm {vm_name} due to {ret}")
            else:
                print("Successfully attach vm {}".format(vm_name))
                # logging.info(f"Successfully attach vm {vm_name}")
                height = ds[1] + 1
                sql3 = "update block_datastore_objs set height= %d where VMFS_datastore = '%s';" % (height, ds[0])
                if type == "file":
                    sql3 = "update datastore_objs set height= %d where NFS_datastore = '%s';" % (height, ds[0])
                database.update_data(sql3)






