
import os
import re
import subprocess
from utils.os.Linux import Executor
import requests

current = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(current))
class NodeExporter(object):
    @staticmethod
    def install_exporter_linux(ip, user, password):
        excutor = Executor(ip, user, password)
        out = excutor.execute("ss -ntlp | grep -o 9100")
        if out != '9100':
            print("node exporter not installed")
            excutor.upload_file(BASE_DIR+os.sep+"monitor"+os.sep+"node_exporter-1.3.1.linux-amd64.tar.gz","/root/")
            excutor.run("tar xvfz /root/node_exporter-1.3.1.linux-amd64.tar.gz")
            # excutor.run("cd /root/node_exporter-1.3.1.linux-amd64/ && nohup ./node_exporter &")
            excutor.upload_file(BASE_DIR+os.sep+"monitor"+os.sep+"nodeexport.sh","/root/")
            excutor.run("chmod +x /root/nodeexport.sh")
            out = excutor.run("/root/nodeexport.sh")
            if re.search("successed",out):
                # excutor.run("curl http://localhost:9100/metrics")
                print("node exporter installed success!!!")
            else:
                excutor.run("curl http://localhost:9100/metrics")
                print("node exporter installed failed!!!")
                exit(1)
        else:
            print("node exporter already installed")
        excutor.close()
        
    @staticmethod
    def register_to_consul(ip,name,id,port,check_url):
        consul_url = 'http://10.226.69.47:8500/v1/agent/service/register'
        headers = dict()
        headers.update({"Accept": "application/json"})
        headers.update({"Content-Type": "application/json"})
        data = {
                "id": id,
                "address": ip,
                "name": name,
                "port": port,
                "tags": ["tm_app"],
                "checks": [{"http": check_url, "interval": "5s"}]
            }
        reponse = requests.put(consul_url,json=data,headers=headers,verify=False)
        print(reponse)
        
    @staticmethod
    def deregister_to_consul(id):
        consul_url = 'http://10.226.69.47:8500/v1/agent/service/deregister/{}'.format(id)
        headers = dict()
        headers.update({"Accept": "application/json"})
        headers.update({"Content-Type": "application/json"})
        requests.put(consul_url,headers=headers,verify=False)

    @staticmethod
    def create_pushgateway_cronjob(ip, user, password,export_node):
        excutor = Executor(ip, user, password)
        cron_file = '* * * * * /root/push_metric.sh {}\n'.format(export_node)
        excutor.run('echo "{}" | crontab -'.format(cron_file))
        excutor.close()
        

