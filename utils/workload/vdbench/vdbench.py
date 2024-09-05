from json.tool import main
import pandas as pd
from collections import defaultdict
import paramiko
from scp import SCPClient
import time
from threading import Thread
import socket
import argparse
from pypsrp.client import Client
from pypsrp.powershell import PowerShell, RunspacePool
from pypsrp.wsman import WSMan
import winrm
import sys
import re
import os
from utils.os.Linux import Executor
current = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(current))
vdparam_file=BASE_DIR+os.sep+"vdbench"+os.sep+"vdparam_file.csv"
vdbench_pusher=BASE_DIR+os.sep+"vdbench"+os.sep+"vdbench_pusher"
class VdParam:
    def __init__(self,node,anchor,depth,width,files,size,openflags,operation,fileio,rdpct,xfersize,fileselect,threads,elapsed,interval):
        self.node = node
        self.anchor = anchor
        self.depth = depth
        self.width = width
        self.files = files
        self.size = size
        self.openflags = openflags
        self.operation = operation
        self.fileio = fileio
        self.rdpct = rdpct
        self.xfersize = xfersize
        self.fileselect = fileselect
        self.threads = threads
        self.elapsed = elapsed
        self.interval = interval

class VdParamRaw:
    def __init__(self,node,lun,openflags,threads,xfersize,rdpct,seekpct,iorate,elapsed,interval):
        self.node = node
        self.lun = lun
        self.openflags = openflags
        self.threads = threads
        self.xfersize = xfersize
        self.rdpct = rdpct
        self.seekpct = seekpct
        self.iorate = iorate
        self.elapsed = elapsed
        self.interval = interval
        
class Vdbench(object):

    def load_csv_data_file(self,df):
        vdparam_list = []
        node_run_data= defaultdict(list)
        # df=pd.read_csv(vdparam_file,encoding='utf-8', usecols=['node','user','password','vdbench','job','anchor','depth', 'width','files','size','openflags','operation','fileio','rdpct','xfersize','fileselect','threads','elapsed','interval'])
        df_node_run_data = df.loc[:, ['node','user','password','vdbench','job']]
        df_node_run_data = df_node_run_data.groupby("node").first()
        df_node_vd_data = df.loc[:, ['node','anchor','depth', 'width','files','size','openflags','operation','fileio','rdpct','xfersize','fileselect','threads','elapsed','interval']]
        for idx, row in df_node_vd_data.iterrows():
            node = row['node']
            anchor = row['anchor']
            depth = row['depth']
            width = row['width']
            files = row['files']
            size = row['size']
            openflags = row['openflags']
            operation = row['operation']
            fileio = row['fileio']
            rdpct = row['rdpct']
            xfersize = row['xfersize']
            fileselect = row['fileselect']
            threads = row['threads']
            elapsed = row['elapsed']
            interval = row['interval']
            vdparam = VdParam(node,anchor,depth,width,files,size,openflags,operation,fileio,rdpct,xfersize,fileselect,threads,elapsed,interval)
            vdparam_list.append(vdparam)
            vdparam_list = sorted(vdparam_list,key=lambda x:x.node)
        for node, grp in df_node_run_data.iterrows():
            node_run_data[node] = [grp['user'],grp['password'],grp['vdbench'],grp['job']]
        return vdparam_list,node_run_data

    def load_csv_data_raw(self,df):
        vdparam_list = []
        node_run_data= defaultdict(list)
        # df=pd.read_csv("vdbench_file.csv",encoding='utf-8', usecols=['node','user','password','vdbench','job','lun','openflags','threads','xfersize','rdpct','seekpct','iorate','elapsed','interval'])
        df_node_run_data = df.loc[:, ['node','user','password','vdbench','job']]
        df_node_run_data = df_node_run_data.groupby("node").first()
        df_node_vd_data = df.loc[:, ['node','lun','openflags','threads','xfersize','rdpct','seekpct','iorate','elapsed','interval']]
        for idx, row in df_node_vd_data.iterrows():
            node = row['node']
            lun = row['lun']
            openflags = row['openflags']
            threads = row['threads']
            xfersize = row['xfersize']
            rdpct = row['rdpct']
            seekpct = row['seekpct']
            iorate = row['iorate']
            elapsed = row['elapsed']
            interval = row['interval']
            vdparam = VdParamRaw(node,lun,openflags,threads,xfersize,rdpct,seekpct,iorate,elapsed,interval)
            vdparam_list.append(vdparam)
            vdparam_list = sorted(vdparam_list,key=lambda x:x.node)
        for node, grp in df_node_run_data.iterrows():
            node_run_data[node] = [grp['user'],grp['password'],grp['vdbench'],grp['job']]
        return vdparam_list,node_run_data

    def asyncs(f):
        def wrapper(*args, **kwargs):
            thr = Thread(target=f, args=args, kwargs=kwargs)
            thr.setDaemon(True)
            thr.start()

        return wrapper

    def generate_vd_file_text_per_node(self,vdparam_list,type):
        vd_file_dict = defaultdict(list)
        for vdparam in vdparam_list:
            key = vdparam.node
            vd_file_dict[key].append(vdparam)
        for node in vd_file_dict:
            i = 0
            fsd_lines = []
            fwd_lines = []
            vdparam_list_per_node = vd_file_dict[node]
            elapsed = vdparam_list_per_node[0].elapsed
            interval = vdparam_list_per_node[0].interval
            for vdparam in vdparam_list_per_node:
                i += 1
                fsd = ""
                if type == "Linux":
                    fsd = "fsd=fsd{},anchor={},depth={},width={},files={},size={},openflags={}\n" .format(i,vdparam.anchor,vdparam.depth,
                    vdparam.width,vdparam.files,vdparam.size,vdparam.openflags)
                else:
                    fsd = "fsd=fsd{},anchor={},depth={},width={},files={},size={}\n" .format(i,vdparam.anchor,vdparam.depth,
                    vdparam.width,vdparam.files,vdparam.size)
                fsd_lines.append(fsd)
                fwd = "fwd=fwd{},fsd=fsd{},rdpct={},xfersize={},fileio={},fileselect={},threads={}\n".format(i,i,vdparam.rdpct,vdparam.xfersize,
                vdparam.fileio,vdparam.fileselect,vdparam.threads)
                fwd_lines.append(fwd)
            with open("{}.txt".format(node), "w") as file1:
                file1.writelines(fsd_lines)
                file1.writelines(fwd_lines)
                file1.write("rd=rd1,fwd=fwd*,fwdrate=max,format=yes,elapsed={},interval={}".format(elapsed,interval) )
        return list(vd_file_dict.keys())

    def generate_vd_file_text_per_node_raw(self,vdparam_list,type):
        vd_file_dict = defaultdict(list)
        for vdparam in vdparam_list:
            key = vdparam.node
            vd_file_dict[key].append(vdparam)
        for node in vd_file_dict:
            i = 0
            sd_lines = []
            wd_lines = []
            vdparam_list_per_node = vd_file_dict[node]
            iorate = vdparam_list_per_node[0].iorate
            elapsed = vdparam_list_per_node[0].elapsed
            interval = vdparam_list_per_node[0].interval
            for vdparam in vdparam_list_per_node:
                i += 1
                sd = ""
                if type == "Linux":
                    sd = "sd=sd{},lun={},openflags={},threads={}\n".format(i,vdparam.lun, vdparam.openflags,vdparam.threads)
                else:
                    sd = "sd=sd{},lun={},threads={}\n".format(i,vdparam.lun,vdparam.threads)
                sd_lines.append(sd)
                wd = "wd=wd{},sd=sd{},xfersize={},rdpct={},seekpct={}\n".format(i,i,vdparam.xfersize,vdparam.rdpct,vdparam.seekpct)
                wd_lines.append(wd)
            with open("{}.txt".format(node), "w") as file1:
                file1.writelines(sd_lines)
                file1.writelines(wd_lines)
                file1.write("rd=run1,wd=wd*,iorate={},elapsed={},interval={}".format(iorate,elapsed,interval))
        return list(vd_file_dict.keys())
        

    def upload_file(self,ip,file,remote_path,vm_user,vm_passwd):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, username=vm_user, password=vm_passwd,timeout=30)
            with SCPClient(ssh.get_transport()) as scp:
                scp.put(file, remote_path,recursive=True)
            ssh.close()
        except Exception as e:
            print(e)
        finally:
            ssh.close()

    def upload_file_windows(self,ip,username,password,file):
        with Client(ip, username=username, password=password,cert_validation=False,ssl=False) as client:
            output, streams, had_errors = client.execute_ps('''$path = "%s"
    if ( -Not (Test-Path -Path $path)) {
        New-Item -Path $path -ItemType Directory
    }
    ''' % "C:\\temp")
            client.copy(file, "C:\\temp\\%s" % file)

    @asyncs
    def execute_ps(self,ip,username,password,cmd):
        print(cmd)
        wsman = WSMan(ip, username=username,
                password=password, ssl=False,cert_validation=False)
        with RunspacePool(wsman) as pool:
            ps = PowerShell(pool)
            ps.add_script(cmd)
            output = ps.invoke()
            outputs = "\n".join([str(s) for s in output])
            print("OUTPUT:%s" % "\n".join([str(s) for s in output]))
            print("ERROR:%s" % "\n".join([str(s) for s in ps.streams.error]))
            return outputs

    @asyncs
    def execute_win_cmd(self,ip,username,password,cmd):
        print(cmd)
        con = winrm.Session('http://{}:5985/wsman'.format(ip), auth=(username, password))
        r = con.run_cmd(cmd)


    @asyncs
    def remote_excute_cmd(self,ip,cmd,vm_user,vm_passwd,nohup=True,result_print=None):
        excutor = Executor(ip, vm_user, vm_passwd)
        excutor.run(cmd)

    def run_vdbench(self,type,action,raw,df):
        vdparam_list = []
        node_run_data= defaultdict(list)
        node_list = []
        if raw:
            vdparam_list,node_run_data = self.load_csv_data_raw(df)
            node_list = self.generate_vd_file_text_per_node_raw (vdparam_list,type)
        else:
            vdparam_list,node_run_data = self.load_csv_data_file(df)
            node_list = self.generate_vd_file_text_per_node(vdparam_list,type)

        if type == "Linux":
            self.run_linux(node_run_data, node_list,action)
        else:
            self.run_windows(node_run_data, node_list,action)

    def run_windows(self,node_run_data, node_list,action):
        if action == "run":
            for node in node_list:
                user = node_run_data[node][0]
                password = node_run_data[node][1]
                self.config_winrm(node,user,password)
                self.upload_file_windows(node,user,password,"{}.txt".format(node))
                self.upload_file_windows(node,user,password,"vdbench_pusher.exe")
                vdbench_path = node_run_data[node][2]
                job = node_run_data[node][3]
                cmd = 'start /b {} -f C:\\temp\\{}.txt | C:\\temp\\vdbench_pusher.exe --gateway http://10.226.112.170:31659 --job {} > stdout.txt 2> stderr.txt'.format(vdbench_path,node,job)
                self.execute_win_cmd(node,user,password,cmd)
            time.sleep(5)
            sys.exit(0)
        if action == "stop":
            for node in node_list:
                user = node_run_data[node][0]
                password = node_run_data[node][1]
                cmd = "taskkill /F /IM vdbench_pusher.exe & taskkill /F /IM java.exe"
                self.execute_win_cmd(node,user,password,cmd)
            time.sleep(5)
            sys.exit(0)

    def config_winrm(self,ip,username,password):
        wsman = WSMan(ip, username=username,
                password=password, ssl=False,cert_validation=False)
        with RunspacePool(wsman) as pool:
            ps = PowerShell(pool)
            ps.add_script('''winrm set winrm/config/service '@{AllowUnencrypted="''' + '''true"}'''+"'")
            ps.add_script('''winrm set winrm/config/service/auth '@{Basic="''' + '''true"}'''+"'")
            ps.add_script('''winrm set winrm/config/client/auth '@{Basic="''' + '''true"}'''+"'")
            ps.add_script('''winrm set winrm/config/client '@{TrustedHosts="''' + '''10.226.112.83"}'''+"'")
            # ps.add_script('''winrm set winrm/config/WinRs '@{IdleTimeout="''' + '''6000"}'''+"'")
            output = ps.invoke()
            # print("OUTPUT:%s" % "\n".join([str(s) for s in output]))
            # print("ERROR:%s" % "\n".join([str(s) for s in ps.streams.error]))

    def run_linux(self,node_run_data, node_list,action):
        if action == "run":
            for node in node_list:
                user = node_run_data[node][0]
                password = node_run_data[node][1]
                self.upload_file(node,"{}.txt".format(node),"/root/",user,password)
                self.upload_file(node,vdbench_pusher,"/root/",user,password)
                vdbench_path = node_run_data[node][2]
                job = node_run_data[node][3]
                cmd =  " nohup sh -c '{} -f {}.txt | /root/vdbench_pusher --gateway http://10.226.112.170:31659 --job {}  >run_vd.txt 2>&1 &'".format(vdbench_path,node,job)
                #cmd = " nohup {} -f {}.txt  >run_vd.txt 2>&1 ".format(vdbench_path,node)
                self.remote_excute_cmd(node,cmd,user,password)
                time.sleep(5)
        if action == "stop":
            for node in node_list:
                user = node_run_data[node][0]
                password = node_run_data[node][1]
                self.upload_file(node,"kill_vdbench.sh","/root/",user,password)
                self.remote_excute_cmd(node,"chmod +x /root/kill_vdbench.sh && /root/kill_vdbench.sh",user,password,nohup=False)
                time.sleep(5)

    def repalce_column_with_value(self,cname,origin_values,replace_values,df=None):
        if df is None:
            df=pd.read_csv(vdparam_file,encoding='utf-8', usecols=['node','user','password','vdbench','job','anchor','depth', 'width','files','size','openflags','operation','fileio','rdpct','xfersize','fileselect','threads','elapsed','interval'])
        df[cname].replace(origin_values,replace_values,inplace=True)
        return df
            
