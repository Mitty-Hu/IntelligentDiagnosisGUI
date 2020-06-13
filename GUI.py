import sys

import paramiko
import os
from PyQt5.QtCore import *
import time

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QDir, pyqtSlot
from diagnosis import *


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        # 文件上传变量

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

        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.slotInit()
        self.customInitUI()
        self.allThreads = []

    def slotInit(self):
        self.actionopen.triggered.connect(self.openDataFile)
        self.actioncolseServer.triggered.connect(self.closeServer)
        self.actionconnectServer.triggered.connect(self.connectServer)
        self.pushButton_Upload.pressed.connect(self.uploadFile)
        self.pushButton_Download.pressed.connect(self.downloadFile)

    def customInitUI(self):
        self.statusBar.showMessage("准备就绪")
        self.progressBar.setValue(0)
        self.textEdit_IP.setPlainText(str(self.ip))
        self.textEdit_PORT.setPlainText(str(self.port))
        self.textEdit_User.setPlainText(str(self.user))
        self.lineEdit_Pwd.setText(self.password)

    # 打开数据文件，获取文件的路径
    def openDataFile(self):
        dataFilePath = QDir.currentPath()
        dataFileName, dataFileType = QFileDialog.getOpenFileName(self, "Open data files", dataFilePath,
                                                                 "*.txt;;All Files(*)")

        (self.local_root, self.file) = os.path.split(dataFileName)
        self.local_file_abs = self.local_root + '/' + self.file
        self.local_result_abs = self.local_root + '/result_' + self.file
        self.remote_file_abs = self.server_root + '/' + self.file
        self.remote_result_abs = self.server_root + '/result_' + self.file
        print(self.local_file_abs + "\n" + self.local_result_abs)
        print(self.remote_file_abs + "\n" + self.remote_result_abs + "\n")
        self.textEdit_ConnectStatus.setPlainText("File Name:" + self.file + "\n" + "File Path:" + self.local_file_abs)

    def connectServer(self):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(self.ip, self.port, self.user, self.password)
            print("连接已建立")
            self.statusBar.showMessage("Server connected")
        except Exception as e:
            print("未能连接到服务器")

    def closeServer(self):
        self.ssh.close()
        print("连接已关闭")
        self.statusBar.showMessage("Server closed")

    # 打开上传子线程
    def uploadFile(self):
        self.thread = upLoadThread()
        self.thread.setFilePath(self.local_file_abs, self.remote_file_abs)
        self.thread.upLoadThread_signal.connect(self.callBack_upLoad)
        self.thread.start()
        self.allThreads.append(self.thread)
        print(self.allThreads)
        self.textEdit_ConnectStatus.setPlainText("Loading...")

        self.thread = showLoadPercentThread()
        self.thread.setFilePath(self.local_file_abs, self.remote_file_abs, self.local_result_abs, self.remote_result_abs)
        self.thread.showLoadPercentThread_signal.connect(self.callBack_progressBar)
        self.thread.start()
        self.allThreads.append(self.thread)
        print(self.allThreads)

    def callBack_upLoad(self):
        self.textEdit_ConnectStatus.setPlainText("Upload Success!")

    def callBack_progressBar(self, percent):
        self.progressBar.setValue(percent)

    def downloadFile(self):
        sftp = paramiko.SFTPClient.from_transport(self.ssh.get_transport())
        sftp = self.ssh.open_sftp()
        f = open(self.local_result_abs, "w")
        f.close()
        sftp.get(self.remote_result_abs, self.local_result_abs)
        self.textEdit_ConnectStatus.setPlainText("Download Success!")


# 上传线程
class upLoadThread(QtCore.QThread):
    #  通过类成员对象定义信号对象
    upLoadThread_signal = pyqtSignal()

    def __init__(self):
        super(upLoadThread, self).__init__()
        self.local_file_abs = '/'
        self.remote_file_abs = '/'
        self.user = "root"
        self.password = "PMgroup8"
        self.port = 22
        self.ip = "39.98.143.89"

    def __del__(self):
        self.wait()

    def setFilePath(self, local, remote):
        self.local_file_abs = local
        self.remote_file_abs = remote


    def run(self):
        print(QThread.currentThreadId())
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(self.ip, self.port, self.user, self.password)
            print("连接已建立")
        except Exception as e:
            print("未能连接到服务器")
        sftp = paramiko.SFTPClient.from_transport(self.ssh.get_transport())
        sftp = self.ssh.open_sftp()
        sftp.put(self.local_file_abs, self.remote_file_abs)

        self.upLoadThread_signal.emit()


# 上传进度条线程
class showLoadPercentThread(QtCore.QThread):
    #  通过类成员对象定义信号对象
    showLoadPercentThread_signal = pyqtSignal(int)

    def __init__(self):
        super(showLoadPercentThread, self).__init__()
        self.user = "root"
        self.password = "PMgroup8"
        self.port = 22
        self.ip = "39.98.143.89"
        self.local_file_abs = '/'
        self.remote_file_abs = '/'

    def __del__(self):
        self.wait()

    def setFilePath(self, local, remote, local_result, remote_result):
        self.local_file_abs = local
        self.remote_file_abs = remote
        self.local_result_abs = local_result
        self.remote_result_abs = remote_result

    def cmd(self, cmd_str='-1'):
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
        kbytes = int(bytes / 1024)
        # print(kbytes)
        return kbytes

    def run(self):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(self.ip, self.port, self.user, self.password)
            print("进度条线程连接已建立")
        except Exception as e:
            print("未能连接到服务器")
        time.sleep(3)
        per = 0
        while per < 99.9:
            server = self.size_server("data")
            local = self.size_local("data")
            per = server / local * 100
            print("transport percent", per)
            self.showLoadPercentThread_signal.emit(int(per))
            time.sleep(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWin = MyMainForm()
    myWin.show()

    sys.exit(app.exec_())
