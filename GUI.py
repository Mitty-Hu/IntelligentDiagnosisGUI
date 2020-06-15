import sys

import paramiko
import os
from PyQt5.QtCore import *
import time
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.cluster import MeanShift, estimate_bandwidth
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtCore import QDir, pyqtSlot,QSize
from diagnosis import *
from visualize import *


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        # 文件上传变量

        self.user = "root"
        self.password = "PMgroup8"
        self.port = 22
        self.ip = "39.98.143.89"
        self.local_root = 'E:/GUI'
        self.server_root = '/home/project'
        self.file = '79.txt'
        self.local_file_abs = self.local_root + '/' + self.file
        self.local_result_abs = self.local_root + '/result.txt'
        self.remote_file_abs = self.server_root + '/data/pred/' + self.file
        self.remote_result_abs = self.server_root + '/result/result.txt'

        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.slotInit()
        self.customInitUI()
        self.allThreads = []

    def slotInit(self):  # 初始化控件的槽函数
        self.actionopen.triggered.connect(self.openDataFile)
        self.actioncolseServer.triggered.connect(self.closeServer)
        self.actionconnectServer.triggered.connect(self.connectServer)
        self.pushButton_Upload.pressed.connect(self.uploadFile)
        self.pushButton_Download.pressed.connect(self.downloadFile)
        self.pushButton_openVisualizationFile.pressed.connect(self.visualizeDataProcess)
        self.radioButton_KMeans.toggled.connect(self.showKMean)
        self.radioButton_GaussianMixture.toggled.connect(self.showGM)
        self.radioButton_1.toggled.connect(self.show1)
        self.radioButton_2.toggled.connect(self.show2)

    def customInitUI(self):  # 初始化一些控件的内容
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
        self.local_result_abs = self.local_root + '/result.txt'
        self.remote_file_abs = self.server_root + '/data/pred/' + self.file
        self.remote_result_abs = self.server_root + '/result/result.txt'
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
        self.progressBar.setValue(25)
        time.sleep(0.3)
        self.progressBar.setValue(50)
        time.sleep(0.6)
        self.progressBar.setValue(75)

        # self.thread = showLoadPercentThread()
        # self.thread.setFilePath(self.local_file_abs, self.remote_file_abs, self.local_result_abs,
        #                        self.remote_result_abs)
        # self.thread.showLoadPercentThread_signal.connect(self.callBack_progressBar)
        # self.thread.start()
        # self.allThreads.append(self.thread)
        # print(self.allThreads)

    def downloadFile(self):
        self.thread = downloadThread()
        self.thread.setDownloadFilePath(self.local_result_abs, self.remote_result_abs)
        self.thread.downloadThread_signal.connect(self.callBack_download)
        self.thread.start()
        self.allThreads.append(self.thread)
        print(self.allThreads)
        self.textEdit_ConnectStatus.setPlainText("Loading...")
        self.progressBar.setValue(0)
        time.sleep(0.2)
        self.progressBar.setValue(30)
        time.sleep(0.2)
        self.progressBar.setValue(60)

    def visualizeDataProcess(self):
        visualizationFilePath = QDir.currentPath()
        visualizationFileName, visualizationFileType = QFileDialog.getOpenFileName(self, "Open visualization files",
                                                                                   visualizationFilePath,
                                                                                   "*.txt;;All Files(*)")
        self.textEdit_ConnectStatus.setPlainText("Doing Visualization...")
        self.thread = visualizationThread()
        self.thread.setFilePath(visualizationFileName)
        self.thread.visualizationThread_signal.connect(self.callBack_visualization)
        self.thread.start()
        self.allThreads.append(self.thread)
        print(self.allThreads)

    def callBack_upLoad(self):
        self.progressBar.setValue(100)
        self.textEdit_ConnectStatus.setPlainText("Upload Success!" + "\n" + "Analysing...")
        self.textEdit_ConnectStatus.setPlainText("Complete Analysis" + "\n" + "Please download result file")

    def callBack_download(self):
        self.progressBar.setValue(100)
        f = open(self.local_result_abs)
        line = f.readline()
        self.textEdit_ConnectStatus.setPlainText("Download Success!" + "\n" + "Prediction Result: " + "\n" + line)
        for thread in self.allThreads:
            if thread.isRunning():
                thread.stop()
            del self.allThreads[:]

    def callBack_progressBar(self, percent):
        self.progressBar.setValue(percent)

    def callBack_visualization(self):
        self.textEdit_ConnectStatus.setPlainText("Complete Visualization")

    def showKMean(self):
        self.label_Figure.clear()
        pix = QPixmap('KMean.png').scaled(self.label_Figure.width(), self.label_Figure.height())
        self.label_Figure.setPixmap(pix)

    def showGM(self):
        self.label_Figure.clear()
        pix = QPixmap('GM.png').scaled(self.label_Figure.width(), self.label_Figure.height())
        self.label_Figure.setPixmap(pix)

    def show1(self):
        self.label_Figure.clear()
        pix = QPixmap('MultiRolling.png').scaled(self.label_Figure.width(), self.label_Figure.height())
        self.label_Figure.setPixmap(pix)

    def show2(self):
        self.label_Figure.clear()
        pix = QMovie("MultiRolling.gif")
        pix.setScaledSize(QSize(681, 581))
        pix.start()
        self.label_Figure.setMovie(pix)





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
        time.sleep(1)
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(self.ip, self.port, self.user, self.password)
            print("连接已建立")
        except Exception as e:
            print("未能连接到服务器")
        sftp = paramiko.SFTPClient.from_transport(self.ssh.get_transport())
        sftp = self.ssh.open_sftp()
        self.ssh.exec_command("rm /home/project/data/pred/*.txt")
        sftp.put(self.local_file_abs, self.remote_file_abs)
        self.ssh.exec_command("bash /home/project/pred.bash")
        self.upLoadThread_signal.emit()


class downloadThread(QtCore.QThread):
    downloadThread_signal = pyqtSignal()

    def __init__(self):
        super(downloadThread, self).__init__()
        self.local_result_abs = '/'
        self.remote_result_abs = '/'
        self.user = "root"
        self.password = "PMgroup8"
        self.port = 22
        self.ip = "39.98.143.89"

    def __del__(self):
        self.wait()

    def setDownloadFilePath(self, local_result, remote_result):
        self.local_result_abs = local_result
        self.remote_result_abs = remote_result

    def run(self):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(self.ip, self.port, self.user, self.password)
            print("连接已建立")
        except Exception as e:
            print("未能连接到服务器")
        sftp = paramiko.SFTPClient.from_transport(self.ssh.get_transport())
        sftp = self.ssh.open_sftp()
        print(self.local_result_abs + "\n" + self.remote_result_abs)
        f = open(self.local_result_abs, "w")
        f.close()
        sftp.get(self.remote_result_abs, self.local_result_abs)
        self.downloadThread_signal.emit()


# 进度条线程
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
        time.sleep(0.5)
        per = 0
        while per < 99.9:
            server = self.size_server("data")
            local = self.size_local("data")
            per = server / local * 100
            print("transport percent", per)
            self.showLoadPercentThread_signal.emit(int(per))
            time.sleep(0.2)


class visualizationThread(QtCore.QThread):
    #  通过类成员对象定义信号对象
    visualizationThread_signal = pyqtSignal()

    def __init__(self):
        super(visualizationThread, self).__init__()
        self.visualizationFileName = '/'

    def __del__(self):
        self.wait()

    def setFilePath(self, fileName):
        self.visualizationFileName = fileName
        print(self.visualizationFileName)

    def run(self):
        print(QThread.currentThreadId())
        KMean(self.visualizationFileName)
        GM(self.visualizationFileName)
        self.visualizationThread_signal.emit()


def KMean(filePath):
    k = 4
    data = pd.read_table(filePath)
    value = data.values
    seed = 9  # 设置随机种子
    clf = KMeans(n_clusters=k, random_state=seed)  # 聚类
    clf.fit(value)  # 拟合模型
    label = clf.labels_
    for i in range(k):
        y = label == i  # 得到boolean矩阵
        z = label[y]
        print(z.size)  # 输出每一类数量
    y_pred = clf.fit_predict(value)
    plt.figure(1)
    plt.subplot(311)
    plt.scatter(value[:, 0], value[:, 1], s=1, c=y_pred)
    plt.xlabel('AGC_Piston_OS (bar)')
    plt.ylabel('Acc_F3_Bot_WR_Z (g)')
    plt.subplot(312)
    plt.scatter(range(len(value)), value[:, 0], s=1, c=y_pred)
    plt.xlabel('t')
    plt.ylabel('AGC_Piston_OS (bar)')
    plt.subplot(313)
    plt.scatter(range(len(value)), value[:, 1], s=1, c=y_pred)
    plt.xlabel('t')
    plt.ylabel('Acc_F3_Bot_WR_Z (g)')
    plt.savefig('KMean.png')


def GM(filePath):
    data = pd.read_table(filePath)
    value = data.values
    k = 4  # 设置聚类数
    gmm = GaussianMixture(n_components=k)
    gmm.fit(value)
    labels = gmm.predict(value)

    for i in range(k):
        y = labels == i  # 得到boolean矩阵
        z = labels[y]
        print(z.size)  # 输出每一类数量
    plt.figure(2)
    plt.subplot(311)
    plt.scatter(value[:, 0], value[:, 1], s=1, c=labels)
    plt.xlabel('AGC_Piston_OS (bar)')
    plt.ylabel('Acc_F3_Bot_WR_Z (g)')
    plt.subplot(312)
    plt.scatter(range(len(value)), value[:, 0], s=1, c=labels)
    plt.xlabel('t')
    plt.ylabel('AGC_Piston_OS (bar)')
    plt.subplot(313)
    plt.scatter(range(len(value)), value[:, 1], s=1, c=labels)
    plt.xlabel('t')
    plt.ylabel('Acc_F3_Bot_WR_Z (g)')
    plt.savefig('GM.png')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWin = MyMainForm()
    myWin.show()

    sys.exit(app.exec_())
