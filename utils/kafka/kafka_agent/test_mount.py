import socket
import subprocess 
NAME = "FGHIJKLMNOPQRSTUVWXYZ"
class ShareMount:

    def run(self, cmd, os_type):
        completed = 0
        if os_type == "Linux":
            completed = subprocess.run([cmd],shell=True)
        if os_type == "Windows":
            completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
        return completed
    
    def test_mount(self,mount_dict, os_type):
        mountsmb = []
        mountnfs = []
        key = ''.join(socket.gethostbyname(socket.gethostname()).split("."))
        if os_type == "Linux":
            mountnfs = mount_dict.get(key)
            i = 0
            for mount_point in mountnfs:
                cmd = "mkdir -p /tmp/data_%d && mount %s /tmp/data_%d" % (i, mount_point, i)
                mount_info = self.run(cmd,"Linux")
                if mount_info.returncode != 0:
                    print("An error occured: %s", mount_info.stderr)
                else:
                    print("Mount {} executed successfully!".format(mount_point))

        if os_type == "Windows":
            mountsmb = mount_dict.get(key)
            i = 0
            for mount_point in mountsmb:
                name = ""
                if i <= 21:
                    name = NAME[i]+":"
                else:
                    lest = i / 22 + 1
                    more = i % 22
                    name = self.repeat_string(NAME[more],lest)+ ":"
                # cmd = '$net = new-object -ComObject WScript.Network;$net.MapNetworkDrive("%s", "%s", $false, "Administrator", "#1Danger0us")'.format(name,mount_point)
                cmd = 'net use %s: "+%s+" Admin@123 /user:administrator /persistent:yes' % (name, mount_point)
                mount_info = self.run(cmd,"Windows")
                if mount_info.returncode != 0:
                    print("An error occured: %s", mount_info.stderr)
                else:
                    print("Mount {} executed successfully!".format(mount_point))
                
    def repeat_string(self , input, no_of_times):
        return input*no_of_times

        

class HomedirMount:
    def test_mount(data):
        pass