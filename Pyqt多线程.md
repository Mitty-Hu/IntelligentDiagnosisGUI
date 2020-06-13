```python
class DialogWindow(QDialog, Ui_Dialog):  
    def __init__(self, parent=None):  
        super(DialogWindow, self).__init__(parent)  
        self.setupUi(self)  

    def update_progressbar(self, p_int):  
        self.progressBar.setValue(p_int) # 更新进度条  
  
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):  
    def __init__(self, parent=None):  
        super(MainWindow, self).__init__(parent)  
        self.setupUi(self)  
        self.count = 0  

    def open_dialog(self):  
        dialog = DialogWindow(self)  
        dialog.show()  
        self.thread = RunThread(self.count)  
        self.count += 1  
        self.thread.update_pb.connect(dialog.update_progressbar) # 关联  
        self.thread.start()  
  
class RunThread(QThread):  
    update_pb = pyqtSignal(int) # 定义更新进度条的信号  
  
    def __init__(self, count):  
        super().__init__()  
        self.count = count  

    def run(self):  
        for i in range(100):  
        print('thread%s' % self.count, i, QThread().currentThreadId())  
        self.update_pb.emit(i)  
        time.sleep(1)  
        pass  
  
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)  
    mainWindow = MainWindow()  
    mainWindow.show()  
    sys.exit(app.exec_())  
```

