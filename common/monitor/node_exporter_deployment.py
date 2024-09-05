
import os
import re
import subprocess
from utils.os.Linux import Executor
import requests
from pypsrp.client import Client

from utils.os.windows import WindowsExecutor

current = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(current))
class NodeHelper(object):
    @staticmethod
    def install_exporter_linux(ip, user, password):
        excutor = Executor(ip, user, password)
        out = excutor.execute("ss -ntlp | grep -o 9100")
        if out != '9100':
            print("node exporter not installed")
            excutor.upload_file(BASE_DIR+os.sep+"common"+os.sep+"monitor"+os.sep+"node_exporter-1.3.1.linux-amd64.tar.gz","/root/")
            excutor.run("tar xvfz /root/node_exporter-1.3.1.linux-amd64.tar.gz")
            # excutor.run("cd /root/node_exporter-1.3.1.linux-amd64/ && nohup ./node_exporter &")
            excutor.upload_file(BASE_DIR+os.sep+"common"+os.sep+"monitor"+os.sep+"nodeexport.sh","/root/")
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

    @staticmethod
    def deploy_kafka_agent(ip, user, password):
        excutor = Executor(ip, user, password)
        excutor.execute("rm -fr /root/kafka_agent*")
        excutor.execute("rm -fr /root/code")
        excutor.upload_file("kafka_agent.zip","/root/")
        excutor.run("unzip /root/kafka_agent.zip -d /root")
        excutor.execute("nohup python3 /root/code/utils/kafka/kafka_agent/kafkaConsumer.py >/root/kafka.log 2>&1 &")
        excutor.close()

    @staticmethod
    def deploy_kafka_agent_windows(ip,user,password):
        excutor = WindowsExecutor(ip,user,password)
        excutor.execute_ps("if(Test-Path 'C:\\temp\\'){Remove-Item -Path 'C:\\temp\\' -Recurse -Force}")
        excutor.upload_file_windows("kafka_agent.zip")
        excutor.unzip_file("C:\\temp\\kafka_agent.zip","C:\\temp\\")
        excutor.execute_cmd("\c python C:\\temp\\code\\utils\\kafka\\kafka_agent\\kafkaConsumer.py >nul 2>&1")
        ret = excutor.execute_cmd("tasklist /FI 'IMAGENAME eq python3.11.exe'")
        if ret:
            print("kafka_agent deploy successfully.")
        else:
            print("kafka_agent deploy failure.")



        

