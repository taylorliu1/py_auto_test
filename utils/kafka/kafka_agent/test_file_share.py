from concurrent.futures import ThreadPoolExecutor
import random
import socket
import string
import os
from threading import Thread
import time
global data_empty
data_empty = ""
NAME = "FGHIJKLMNOPQRSTUVWXYZ"
def generate_random_string(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
    
def create_folder(folder_path, depth):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path,777)
    if depth == 0:
        return folder_path
    folder_path = folder_path + os.sep + generate_random_string(1)
    depth = depth - 1
    return create_folder(folder_path, depth)

def repeat_string(input, no_of_times):
    return input*no_of_times
class FileShare:

    def generate_file_action(self, folder,retry,depth,size):
        if not os.path.exists(folder):
            try:
                os.mkdir(folder)
            except:
                pass
        foldername = create_folder(folder,depth)
        if foldername == "":
            foldername = folder
        i  = 0
        global data_empty
        while i < retry:
            file_name = foldername + os.sep + generate_random_string(66)
            file = open(file_name, "w")
            content_random = generate_random_string(24)
            data_empty += content_random
            file.write(data_empty)
            file.seek(size)
            file.write("What a big hole!!!!")
            file.close()
            if len(data_empty.encode()) < 10485760:
                with open(file_name, "r+") as file1:
                    print(file1.read())
            i += 1

    def test_file_share(self, num, retry, duration, depth, size, os_type, mount_dict):
            mountsmb = []
            mountnfs = []
            tasks = []
            key = ''.join(socket.gethostbyname(socket.gethostname()).split("."))
            if os_type == "Linux":
                mountnfs = mount_dict.get(key)
                for index, value in enumerate(mountnfs):
                    txt = generate_random_string(10)
                    name = "/tmp/data_%d/FILE_%s" % (index,txt)
                    for i in range(0, num):
                        thread=Thread(target=self.generate_file_action,args=(name,retry,depth,size))
                        thread.start()
                        tasks.append(thread)
                if duration != 0:
                    time.sleep(duration*60)
                else:
                    for t in tasks:
                        t.join()
            if os_type == "Windows":
                mountsmb = mount_dict.get(key)
                for i, value in enumerate(mountsmb):
                    txt = generate_random_string(10)
                    name = ""
                    if i <= 21:
                        name = NAME[i]+ ":\FILE_" + txt
                    else:
                        lest = i / 22 + 1
                        more = i % 22
                        name = repeat_string(NAME[more],lest)+ ":\FILE_" + txt
                    for i in range(0, num):
                        thread=Thread(target=self.generate_file_action,args=(name,retry,depth,size))
                        thread.start()
                        tasks.append(thread)
                if duration != 0:
                    time.sleep(duration*60)
                else:
                    for t in tasks:
                        t.join()




# if __name__ == '__main__':
#     file_share = FileShare()
#     file_share.test_file_share(2,10,0,2,1000,"Windows",{"19216811021":["test"]})


