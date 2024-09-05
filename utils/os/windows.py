from pypsrp.client import Client
from pypsrp.powershell import PowerShell, RunspacePool
from pypsrp.wsman import WSMan
import winrm

class WindowsExecutor(object):
    def __init__(self,host,user,password):
        self.wsman = WSMan(host, username=user,password=password, ssl=False,cert_validation=False)
        self.winrm = winrm.Session('http://' + host + ':5985/wsman', auth=(user, password))
        self.host = host
        self.user = user
        self.password = password
        self.set_network()
        self.config_winrm(host,user,password)

    def execute_ps(self, cmd):
        with RunspacePool(self.wsman) as pool:
            ps = PowerShell(pool)
            ps.add_script(cmd)
            output = ps.invoke()
            outputs = "\n".join([str(s) for s in output])
            print("OUTPUT:%s" % "\n".join([str(s) for s in output]))
            print("ERROR:%s" % "\n".join([str(s) for s in ps.streams.error]))
            return outputs
    
    def execute_cmd(self, cmd):
        ret = self.winrm.run_cmd(cmd)
        print(ret.std_out.decode())
        
    def upload_file_windows(self,file):
        with Client(self.host, username=self.user, password=self.password,cert_validation=False,ssl=False) as client:
            output, streams, had_errors = client.execute_ps('''$path = "%s"
    if ( -Not (Test-Path -Path $path)) {
        New-Item -Path $path -ItemType Directory
    }
    ''' % "C:\\temp")
            client.copy(file, "C:\\temp\\%s" % file)

    def unzip_file(self, path_to_zip,destination_folder):
        unzip_command = 'Expand-Archive -Path {0} -DestinationPath {1}'.format(path_to_zip,destination_folder)
        self.execute_ps(unzip_command)

    def config_winrm(self,ip,username,password):
        wsman = WSMan(ip, username=username,
                password=password, ssl=False,cert_validation=False)
        with RunspacePool(wsman) as pool:
            ps = PowerShell(pool)
            ps.add_script("winrm quickconfig -q")
            ps.add_script('''winrm set winrm/config/service/auth '@{Basic="''' + '''true"}'''+"'")
            ps.add_script('''winrm set winrm/config/client/auth '@{Basic="''' + '''true"}'''+"'")
            #ps.add_script('''winrm set winrm/config/client '@{TrustedHosts="''' + '''10.226.69.187"}'''+"'")
            ps.add_script('''winrm set winrm/config/service '@{AllowUnencrypted="''' + '''true"}'''+"'")
            output = ps.invoke()
            print("OUTPUT:%s" % "\n".join([str(s) for s in output]))
            print("ERROR:%s" % "\n".join([str(s) for s in ps.streams.error]))

    def set_network(self):
        self.execute_ps("Set-NetConnectionProfile -InterfaceAlias Ethernet0 -NetworkCategory 'Private'")