import re
import paramiko
import socket
from scp import SCPClient
import time
class Executor(object):
    def __init__(self, hostname, username, key, debug=False,set_prompt=False,dis=False):
        self.debug = debug
        self.dis = dis
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname, username=username, password=key,
                look_for_keys=False, compress=True)

        self.chan = self.client.invoke_shell()
        self.chan.settimeout(2)
        self.prompt_regex = "# $"
        if set_prompt:
            self.set_prompt()

    def set_prompt(self):
        prompt = "test:# "
        self.chan.send('export PS1="%s" PS2=""\n' % prompt)
        self.prompt_regex = re.escape(prompt) + '$'
        self.read()

    def execute(self, cmd):
        ssh_stdin, ssh_stdout, ssh_stderr = self.client.exec_command(cmd)
        return ssh_stdout.read().decode().strip()

    def run(self, cmdline):
        # run the command
        cmdline += "\n"
        self.chan.send(cmdline)

        response = self.read()
        m = re.match(re.escape(cmdline) + "(.*)" + self.prompt_regex, response)

        # always return something
        if m:
            return m.group(1)
        else:
            return response

    def recv(self, how_much = 4096):
        try:
            data = self.chan.recv(how_much)
            # print("recv %d bytes: %s" % (len(data), repr(data)))
            if self.dis:
                print("%s" % (data.decode()))
            return data
        except socket.timeout:
            return None

    def read(self):
        data = ''
        buf = self.recv()

        while not re.search(self.prompt_regex, data):
            if buf is not None:
                data += buf.decode()
            buf = self.recv()

        # print("%s" % data)
        return data

    def open_sftp(self):
        return self.client.open_sftp()

    def close(self):
        try: self.chan.close()
        except: pass

        try: self.client.close()
        except: pass

    def upload_file(self,file,remote_path):
        try:
            with SCPClient(self.client.get_transport()) as scp:
                scp.put(file, remote_path,recursive=True)
        except Exception as e:
            print(e)

    def read_expect_promt(self,expect):
        data = ''
        buf = self.recv()
        retry_cnt = 20

        while not re.search(expect, data):
            if buf is not None:
                data += buf.decode()
            buf = self.recv()
            time.sleep(1)
            retry_cnt = retry_cnt -1
            if retry_cnt == 0:
                print ("run command failure expect: "+ "{}".format(expect))
                print("%s" % data)
                exit(1)
        # print("%s" % data)
        return data

    def run_with_expect_prompt(self,cmdline,expect_answer):            
        cmdline += "\n"
        self.chan.send(cmdline)
        for expect,answer in expect_answer:
            self.read_expect_promt(expect)
            answer += "\n"
            self.chan.send(answer)
        response = self.read()
        print(response)

    def create_vdisk(self):
        cmd = "fdisk -l|grep -w Disk|grep sd|tail -n +2|awk -F ' ' '{print $2}'"
        out = self.execute(cmd)
        ret = out.split("\n")
        i = 0
        for disk_name in ret:
            i += 1
            dir = "mkdir /mnt/test{}".format(i)
            self.execute(dir)
            cmd = "fdisk {}".format(disk_name[:-1])
            expect_answer=[("\): ","n"),("\): ",""),("\): ",""),("\): ",""),("\): ",""),("\): ","w")]
            self.run_with_expect_prompt(cmd,expect_answer)           
            fs = disk_name[:-1]+"1"           
            self.execute("mkfs.ext4 {}".format(fs))
            self.execute("mount {} /mnt/test{}".format(fs, i))

    def create_vdisk_nvme(self):
        cmd = "fdisk -l|grep -w Disk|grep nvme|tail -n +2|awk -F ' ' '{print $2}'"
        out = self.execute(cmd)
        ret = out.split("\n")
        i = 0
        for disk_name in ret:
            i += 1
            dir = "mkdir /mnt/test{}".format(i)
            self.execute(dir)
            cmd = "fdisk {}".format(disk_name[:-1])
            expect_answer=[("\): ","n"),("\): ",""),("\): ",""),("\): ",""),("\): ",""),("\): ","w")]
            self.run_with_expect_prompt(cmd,expect_answer)           
            fs = disk_name[:-1]+"1"           
            self.execute("mkfs.ext4 {}".format(fs))
            self.execute("mount {} /mnt/test{}".format(fs, i))


