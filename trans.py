import paramiko
import os
import sys
import getpass
import threading,multiprocessing
import time
from multiprocessing import Process
print("\033[32;1m****开始配置目标机器信息*****\033[0m")

class Tools(object):
    def __init__(self):
        self.user = "root"
        self.password = "PMgroup8"
        self.port = 22
        self.ip = "39.98.143.89"
        self.local_root = 'E:/course/研究生/工业智能维护与预知诊断/hw3/data'
        self.server_root = '/home/project/data'
        self.file = '046.txt'
        self.local_file_abs = self.local_root + '/' + self.file
        self.local_result_abs = self.local_root + '/result_' + self.file
        self.remote_file_abs = self.server_root + '/' + self.file
        self.remote_result_abs = self.server_root + '/result_' + self.file
    def set(self):
        self.ip = input("服务器IP:")
        self.user = input("登录账号:")
        self.password = input("登录密码:")
        self.local_root = input("本地根目录")
        self.server_root = input("服务器根目录")
        self.file = input("待分析文件:")
    def connect(self):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(self.ip, self.port, self.user, self.password)
            print("连接已建立")
        except Exception as e:
            print("未能连接到服务器")
    def cmd(self, cmd_str = '-1'):
        if cmd_str == '-1':
            cmd_str = input("请输入要执行的命令:>>")
        # print(cmd_str)
        _, stdout, _ = self.ssh.exec_command(cmd_str)
        return stdout
    def size_server(self, file="data"):
        if file == "data":
            cmd_str = 'du --apparent-size ' + self.remote_file_abs
        if file == "result":
            cmd_str = 'du --apparent-size ' + self.remote_result_abs
        stdout = self.cmd(cmd_str)
        size_server = stdout.readlines()[0].split()[0]
        # print(size_server)
        kbytes = int(size_server)
        return kbytes
    def size_local(self, file="data"):
        if file == "data":
            bytes = os.path.getsize(self.local_file_abs)
        if file == "result":
            bytes = os.path.getsize(self.local_result_abs)
        kbytes = int(bytes/1024)
        # print(kbytes)
        return kbytes
    def input(self):
        self.local_file_abs = self.local_root + '/' + self.file
        self.local_result_abs = self.local_root + '/result_' + self.file
        self.remote_file_abs = self.server_root + '/' + self.file
        self.remote_result_abs = self.server_root + '/result_' + self.file
    def put(self):
        sftp = paramiko.SFTPClient.from_transport(self.ssh.get_transport())
        sftp = self.ssh.open_sftp()
        self.input()
        p = Process(target=print_per, args=("data",))
        p.start()
        sftp.put(self.local_file_abs,self.remote_file_abs)
        p.terminate()
        p.join()
    def get(self):
        sftp = paramiko.SFTPClient.from_transport(self.ssh.get_transport())
        sftp = self.ssh.open_sftp()
        self.input()
        f = open(self.local_result_abs, "w")
        f.close()
        sftp.get(self.remote_result_abs,self.local_result_abs)
    def close(self):
        self.ssh.close()
        print("连接关闭")

obj = Tools()

def print_per(file):
    global obj
    obj2 = Tools()
    getattr(obj2, "connect")()
    obj2.local_file_abs = obj.local_file_abs
    obj2.local_result_abs = obj.local_result_abs
    obj2.remote_file_abs = obj.remote_file_abs
    obj2.remote_result_abs = obj.remote_result_abs
    per = 0
    while per < 99:
        server = obj2.size_server(file)
        local = obj2.size_local(file)
        if file == "data":
            per = server / local * 100
        if file == "result":
            per = local / server * 100
        print("transport percent", per)
        time.sleep(5)
    getattr(obj2, "close")()

if __name__ == "__main__":
    msg = '''\033[32;1m
    修改信息 >>输入set
    执行命令 >>输入cmd
    上传文件 >>输入put
    下载文件 >>输入get
    退出     >>输入q\033[0m
    '''
    getattr(obj, "connect")()
    while True:
        print(msg)
        inp = input("action:>>")
        if hasattr(obj,inp):
            try:
                getattr(obj,inp)()
            except:
                pass
        if inp == "q":
            getattr(obj,"close")()
            exit()
        else:
            print("没有该选项，请重新输入:>>")