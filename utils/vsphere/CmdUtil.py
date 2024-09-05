import re
import string

import paramiko


class CMD(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def exec_command(self, ip, command, return_need=True, pty_bool=False):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(ip, username=self.username, password=self.password, timeout=30)
        except:
            print("connect to {} error!!!".format(ip))
            return
        stdin, stdout, stderr = client.exec_command(command, get_pty=pty_bool)
        if return_need:
            out = stdout.read().decode().strip()
            client.close()
            return out
        client.close()
