from kafka import KafkaConsumer
import sys
import subprocess
import ctypes, sys,subprocess
import socket
import struct
from test_mount import ShareMount,HomedirMount
import json

from test_file_share import FileShare
from test_command import Command
from test_file_share_zero import FileShareZero

def get_host_ip():
      return socket.gethostbyname(socket.gethostname())

# def ip2int(addr):
#       return struct.unpack("!I",socket.inet_aton(addr))[]
      
def is_admin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False
        
def os_type():
    if sys.platform.startswith('linux'):
        return "Linux"
    else:
        return "Windows"

def run_test_mount():
     pass

def get_func(case):
    if case == "test-share-mount":
        share_mount = ShareMount()
        return getattr(share_mount,'test_mount')
    elif case == "test-homedir-mount":
         homedir_mount = HomedirMount()
         return getattr(homedir_mount,'test_mount')
    elif case == "test-file-share":
         file_share = FileShare()
         return getattr(file_share,'test_file_share')
    elif case == "test-command":
         command = Command()
         return getattr(command,'test_command')
    elif case == "test-file-share-zero":
         file_share_zero = FileShareZero()
         return getattr(file_share_zero,'test_file_share_zero')
    
         
    
     
def start_consumer():
    # i = str(ip2int(get_host_ip()))
    topic = os_type()
    print(os_type())
    consumer = KafkaConsumer(topic, bootstrap_servers = '172.16.65.3:9092')
    consumer.subscribe([topic])

    while True:
        # Poll for new messages from Kafka
        msg = consumer.poll(1.0)

        # Check if we have a message
        if msg == {} or not msg:
            continue
        # if msg.error():
        #     print("Consumer error: {}".format(msg.error()))
        #     continue
        print(msg)
        # Get a header value by key
        record=msg[list(msg.keys())[0]][0]
        header = record.headers
        # Check if header exists
        if header is not None: 
            print(header) 
            
        # Parse message value 
        value=json.loads(record.value)
        print(value)
        func = get_func (header[0][1].decode('utf-8'))
        if func:
            func(value,topic)

    # Close consumer 
    consumer.close()
    
    # for msg in consumer:
    #     msg = consumer.poll(1.0)
    #     print(msg.value)
    #     print("topic = %s" % msg.topic) # topic default is string
    #     print("case= %s" % msg.headers[0][1])
    #     func = get_func (msg.headers[0][1])
    #     func(msg.value,topic)
    #     if is_admin():
    #         cmd = msg.value.decode("utf-8")
    #         cmd = cmd.replace("\"","")
    #         print(cmd)
    #         p = subprocess.Popen(
	# 			cmd,
	# 			shell=1,
	# 			stdout=subprocess.PIPE,
	# 			stderr=subprocess.STDOUT
	# 		)
    #         p.communicate()
    #     else:
	# 		# Re-run the program with admin rights
    #         ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
 
if __name__ == '__main__':
    start_consumer()


