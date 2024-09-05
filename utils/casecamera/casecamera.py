import argparse
import subprocess
import sys
from model import OSEnum,ARRAYEnum

class Casecamera(object):
    def __init__(self, case_name, atype, htype, hosts,hpasswd,switchs,array,dashboard_name,vdbench_job,vc,vcuser,vcpasswd,charbench_job):
        self.cmd = "/root/case_camera/case_camera.py --dashboard_name {}".format(dashboard_name)
        if OSEnum.LINUX == htype:
            self.cmd += " --linux {}".format(hosts) + " --linux_password {}".format(hpasswd)
        elif OSEnum.WINDOWS == htype:
            self.cmd += " --windows {}".format(hosts) + " --windows_password {}".format(hpasswd)
        if ARRAYEnum.POWERSTORE == atype:
            self.cmd += " --powerstore {}".format(array)
        if switchs != "X":
            self.cmd += " --switch {}".format(",".join(switchs))
        if vdbench_job != "X":
            self.cmd += " --vdbench_file_job {}".format(vdbench_job)
        if vc != "X":
            self.cmd += " --vcenter {0} --vcenter_username {1} --vcenter_password {2}".format(vc, vcuser, vcpasswd)
        if charbench_job != "X":
            self.cmd += " --charbench_job {}".format(charbench_job)

    def start(self, start_time):
        cmd = self.cmd + " --time '{}' --command start".format(start_time)
        print(cmd)
        pi= subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
        print(pi.stdout.read())
        
    
    def stop(self, stop_time):
        cmd = self.cmd + " --time '{}' --command stop".format(stop_time)
        print(cmd)
        pi= subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
        print(pi.stdout.read())
        
def help_parser():
    parser = argparse.ArgumentParser(
        description='Standard Arguments for casecamera')
    
    parser.add_argument('-case_name','--case_name',action='store',required=True)

    parser.add_argument('-array_type','--atype',action='store',required=True)

    parser.add_argument('-host_type','--htype', action='store',required=True)

    parser.add_argument('-hosts','--hosts', action='store',required=True)

    parser.add_argument('-host_passwd','--host_passwd', action='store',required=True)

    parser.add_argument('-switchs','--switchs', action='store',required=False)

    parser.add_argument('-array_name','--array', action='store',required=True)

    parser.add_argument('-dashboard_name','--dashboard_name', action='store',required=True)

    parser.add_argument('-vdbench_job','--vdbench_job', action='store',required=False)

    parser.add_argument('-vc','--vc', action='store',required=False)

    parser.add_argument('-vcuser','--vcuser', action='store',required=False)

    parser.add_argument('-vcpasswd','--vcpasswd', action='store',required=False)

    parser.add_argument('-charbench_job','--charbench_job', action='store',required=False)

    parser.add_argument('-start_time','--start_time', action='store',required=True)

    parser.add_argument('-end_time','--end_time', action='store',required=True)

    return parser



if __name__ == '__main__':
    parser = help_parser()
    parser = parser.parse_args()
    case_name = parser.case_name
    atype = parser.atype
    htype = parser.htype
    hosts = parser.hosts
    hpasswd = parser.host_passwd
    switchs = parser.switchs
    array = parser.array
    dashboard_name = parser.dashboard_name
    vdbench_job = parser.vdbench_job
    vc = parser.vc
    vcuser = parser.vcuser
    vcpasswd = parser.vcpasswd
    charbench_job = parser.charbench_job
    start_time = parser.start_time
    end_time = parser.end_time
    casecamera = Casecamera(case_name, atype, htype, hosts,hpasswd,switchs,array,dashboard_name,vdbench_job,vc,vcuser,vcpasswd,charbench_job)
    casecamera.start(start_time)
    casecamera.stop(end_time)