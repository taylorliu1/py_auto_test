from kafka import KafkaConsumer
import sys
import subprocess
import ctypes, sys,subprocess

class Command:
    def is_admin(self):
    	try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    def test_command(self, msg, os_type):
        cmd = msg.replace("\"","")
        print(cmd)
        if os_type == "Windows":
            if self.is_admin()==False:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        p = subprocess.Popen(
            cmd,
            shell=1,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        p.communicate()