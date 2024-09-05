from kafka import KafkaProducer
import json
import socket
import struct
from time import sleep

class MessageProducer:
    broker = ""
    topic = ""
    producer = None

    def __init__(self, broker, topic):
        self.broker = broker
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers=self.broker,
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        acks='all',
        retries = 3)
    
    def send_msg(self, msg, headers):
        print("sending message...")
        try:
            future = self.producer.send(self.topic,msg,headers=headers)
            self.producer.flush()
            future.get(timeout=60)
            print("message sent successfully...")
            return {'status_code':200, 'error':None}
        except Exception as ex:
            return ex

# broker = '172.16.20.12:9092'

# def ip2int(addr):
#     return struct.unpack("!I", socket.inet_aton(addr))[0]

# centos_ipstart = "172.16.98.2"
# centos_ipend = "172.16.98.101"
# centos_ipstart_int = ip2int(centos_ipstart)
# centos_ipend_int = ip2int(centos_ipend)


# win_ipstart = "172.16.98.102"
# win_ipend = "172.16.98.201"
# win_ipstart_int = ip2int(win_ipstart)
# win_ipend_int = ip2int(win_ipend)

# # topic = 'py-test-topic'+str(centos_ipstart_int)
# # message_producer = MessageProducer(broker,topic)
# # print(topic)
# # data = "copy C:\\kafka\\getip.py C:\\"
# # resp=message_producer.send_msg(data)
# nfspathlst = ["172.16.44.207:/test1","172.16.44.207:/test2","172.16.44.207:/test3","172.16.44.206:/test4","172.16.44.206:/test5","172.16.44.206:/test6"]
# i = 0
# for obj in range(centos_ipstart_int,centos_ipend_int+1):
#     topic = 'py-test-topic'+str(obj)
#     message_producer = MessageProducer(broker,topic)
#     nfsindex = i%len(nfspathlst)
#     data = "mkdir -p /tmp/data_"+str(i)+" && mount "+nfspathlst[nfsindex]+" /tmp/data_"+str(i)
#     path = "/tmp/data_"+str(i)
#     data1 = "sed -i 's%path%"+path+"%g' /root/vdbench50407/vd/create_files"
#     run_vd = "cd /root/vdbench50407/vd && ./vdbench -f create_files"
#     resp=message_producer.send_msg(data)
#     print(resp)
#     sleep(10)
#     resp1=message_producer.send_msg(data1)
#     print(resp1)
#     resp2=message_producer.send_msg(run_vd)
#     print(resp2)
#     i = i+1

# j=0
# smbpathlst = ["\\172.16.44.207\clone","\\172.16.44.207\snap","\\172.16.44.207\test1","\\172.16.44.207\test2","\\172.16.44.207\test3","\\172.16.44.206\test4","\\172.16.44.206\test5","\\172.16.44.206\test6"]
# for obj in range(win_ipstart_int,win_ipend_int+1):
#     topic = 'py-test-topic'+str(obj)
#     message_producer = MessageProducer(broker,topic)
#     smbindex = j%len(smbpathlst)
#     data = "net use T: "+smbpathlst[smbindex]+" Admin@123 /user:administrator /persistent:yes && C:\\vdbench50407\\vd\\vdbench -f C:\\vdbench50407\\vd\\create_files"
#     resp=message_producer.send_msg(data)
#     print(resp)
#     j = j+1
    
                
