# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diagnosis.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1235, 719)
        MainWindow.setMinimumSize(QtCore.QSize(1235, 719))
        MainWindow.setMaximumSize(QtCore.QSize(1231, 719))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/icons8-machine-learning-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setIconSize(QtCore.QSize(36, 36))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dockWidget_10 = QtWidgets.QDockWidget(self.centralwidget)
        self.dockWidget_10.setGeometry(QtCore.QRect(0, -3, 701, 641))
        self.dockWidget_10.setAutoFillBackground(True)
        self.dockWidget_10.setStyleSheet("QDockWidget > QWidget {\n"
"    border: 1px solid black;\n"
"}")
        self.dockWidget_10.setFloating(False)
        self.dockWidget_10.setObjectName("dockWidget_10")
        self.dockWidgetContents_13 = QtWidgets.QWidget()
        self.dockWidgetContents_13.setObjectName("dockWidgetContents_13")
        self.label_Figure = QtWidgets.QLabel(self.dockWidgetContents_13)
        self.label_Figure.setGeometry(QtCore.QRect(13, 11, 681, 581))
        self.label_Figure.setMinimumSize(QtCore.QSize(681, 581))
        self.label_Figure.setMaximumSize(QtCore.QSize(681, 581))
        self.label_Figure.setText("")
        self.label_Figure.setObjectName("label_Figure")
        self.dockWidget_10.setWidget(self.dockWidgetContents_13)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1235, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(48, 48))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setToolTip("")
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.dockWidget_Parameter = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_Parameter.setMinimumSize(QtCore.QSize(250, 42))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.dockWidget_Parameter.setPalette(palette)
        self.dockWidget_Parameter.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dockWidget_Parameter.setAutoFillBackground(True)
        self.dockWidget_Parameter.setStyleSheet("QDockWidget > QWidget {\n"
"    border: 1px solid black;\n"
"}")
        self.dockWidget_Parameter.setObjectName("dockWidget_Parameter")
        self.dockWidgetContents_11 = QtWidgets.QWidget()
        self.dockWidgetContents_11.setObjectName("dockWidgetContents_11")
        self.label_SJTUlogo = QtWidgets.QLabel(self.dockWidgetContents_11)
        self.label_SJTUlogo.setGeometry(QtCore.QRect(-10, 530, 271, 91))
        self.label_SJTUlogo.setText("")
        self.label_SJTUlogo.setPixmap(QtGui.QPixmap("icon/SJTUlogo.png"))
        self.label_SJTUlogo.setObjectName("label_SJTUlogo")
        self.line = QtWidgets.QFrame(self.dockWidgetContents_11)
        self.line.setGeometry(QtCore.QRect(10, 520, 235, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_Visualization = QtWidgets.QLabel(self.dockWidgetContents_11)
        self.label_Visualization.setGeometry(QtCore.QRect(10, 10, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_Visualization.setFont(font)
        self.label_Visualization.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Visualization.setObjectName("label_Visualization")
        self.label_KMeans = QtWidgets.QLabel(self.dockWidgetContents_11)
        self.label_KMeans.setGeometry(QtCore.QRect(10, 60, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_KMeans.setFont(font)
        self.label_KMeans.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_KMeans.setObjectName("label_KMeans")
        self.label_GaussianMixture = QtWidgets.QLabel(self.dockWidgetContents_11)
        self.label_GaussianMixture.setGeometry(QtCore.QRect(10, 140, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_GaussianMixture.setFont(font)
        self.label_GaussianMixture.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_GaussianMixture.setObjectName("label_GaussianMixture")
        self.radioButton_k = QtWidgets.QRadioButton(self.dockWidgetContents_11)
        self.radioButton_k.setGeometry(QtCore.QRect(30, 100, 61, 19))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(12)
        self.radioButton_k.setFont(font)
        self.radioButton_k.setObjectName("radioButton_k")
        self.radioButton_Sample = QtWidgets.QRadioButton(self.dockWidgetContents_11)
        self.radioButton_Sample.setGeometry(QtCore.QRect(130, 100, 91, 19))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(12)
        self.radioButton_Sample.setFont(font)
        self.radioButton_Sample.setObjectName("radioButton_Sample")
        self.radioButton_k_2 = QtWidgets.QRadioButton(self.dockWidgetContents_11)
        self.radioButton_k_2.setGeometry(QtCore.QRect(30, 190, 61, 19))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(12)
        self.radioButton_k_2.setFont(font)
        self.radioButton_k_2.setObjectName("radioButton_k_2")
        self.radioButton_Sample_2 = QtWidgets.QRadioButton(self.dockWidgetContents_11)
        self.radioButton_Sample_2.setGeometry(QtCore.QRect(130, 190, 91, 19))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(12)
        self.radioButton_Sample_2.setFont(font)
        self.radioButton_Sample_2.setObjectName("radioButton_Sample_2")
        self.label_MeanShift = QtWidgets.QLabel(self.dockWidgetContents_11)
        self.label_MeanShift.setGeometry(QtCore.QRect(10, 230, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_MeanShift.setFont(font)
        self.label_MeanShift.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_MeanShift.setObjectName("label_MeanShift")
        self.radioButton_Sample_3 = QtWidgets.QRadioButton(self.dockWidgetContents_11)
        self.radioButton_Sample_3.setGeometry(QtCore.QRect(30, 280, 91, 19))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(12)
        self.radioButton_Sample_3.setFont(font)
        self.radioButton_Sample_3.setObjectName("radioButton_Sample_3")
        self.dockWidget_Parameter.setWidget(self.dockWidgetContents_11)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_Parameter)
        self.dockWidget_Server = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_Server.setMinimumSize(QtCore.QSize(271, 350))
        self.dockWidget_Server.setMaximumSize(QtCore.QSize(524287, 350))
        self.dockWidget_Server.setBaseSize(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.dockWidget_Server.setPalette(palette)
        self.dockWidget_Server.setAcceptDrops(False)
        self.dockWidget_Server.setAutoFillBackground(True)
        self.dockWidget_Server.setStyleSheet("QDockWidget > QWidget {\n"
"    border: 1px solid black;\n"
"}")
        self.dockWidget_Server.setInputMethodHints(QtCore.Qt.ImhNone)
        self.dockWidget_Server.setFloating(False)
        self.dockWidget_Server.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_Server.setObjectName("dockWidget_Server")
        self.dockWidgetContents_10 = QtWidgets.QWidget()
        self.dockWidgetContents_10.setObjectName("dockWidgetContents_10")
        self.textEdit_IP = QtWidgets.QTextEdit(self.dockWidgetContents_10)
        self.textEdit_IP.setGeometry(QtCore.QRect(10, 40, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_IP.setFont(font)
        self.textEdit_IP.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit_IP.setObjectName("textEdit_IP")
        self.label_IP = QtWidgets.QLabel(self.dockWidgetContents_10)
        self.label_IP.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_IP.setFont(font)
        self.label_IP.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_IP.setObjectName("label_IP")
        self.label_PORT = QtWidgets.QLabel(self.dockWidgetContents_10)
        self.label_PORT.setGeometry(QtCore.QRect(140, 10, 51, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_PORT.setFont(font)
        self.label_PORT.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_PORT.setObjectName("label_PORT")
        self.textEdit_PORT = QtWidgets.QTextEdit(self.dockWidgetContents_10)
        self.textEdit_PORT.setGeometry(QtCore.QRect(140, 40, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_PORT.setFont(font)
        self.textEdit_PORT.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit_PORT.setObjectName("textEdit_PORT")
        self.pushButton_Upload = QtWidgets.QPushButton(self.dockWidgetContents_10)
        self.pushButton_Upload.setGeometry(QtCore.QRect(30, 170, 191, 48))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Upload.setFont(font)
        self.pushButton_Upload.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/icons8-upload-to-cloud-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Upload.setIcon(icon1)
        self.pushButton_Upload.setIconSize(QtCore.QSize(36, 36))
        self.pushButton_Upload.setObjectName("pushButton_Upload")
        self.pushButton_Download = QtWidgets.QPushButton(self.dockWidgetContents_10)
        self.pushButton_Download.setGeometry(QtCore.QRect(30, 230, 191, 48))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Download.setFont(font)
        self.pushButton_Download.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/icons8-download-from-cloud-80.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Download.setIcon(icon2)
        self.pushButton_Download.setIconSize(QtCore.QSize(36, 36))
        self.pushButton_Download.setObjectName("pushButton_Download")
        self.progressBar = QtWidgets.QProgressBar(self.dockWidgetContents_10)
        self.progressBar.setGeometry(QtCore.QRect(30, 290, 221, 20))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_User = QtWidgets.QLabel(self.dockWidgetContents_10)
        self.label_User.setGeometry(QtCore.QRect(10, 80, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_User.setFont(font)
        self.label_User.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_User.setObjectName("label_User")
        self.textEdit_User = QtWidgets.QTextEdit(self.dockWidgetContents_10)
        self.textEdit_User.setGeometry(QtCore.QRect(10, 110, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_User.setFont(font)
        self.textEdit_User.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit_User.setObjectName("textEdit_User")
        self.label_User_2 = QtWidgets.QLabel(self.dockWidgetContents_10)
        self.label_User_2.setGeometry(QtCore.QRect(140, 80, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_User_2.setFont(font)
        self.label_User_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_User_2.setObjectName("label_User_2")
        self.lineEdit_Pwd = QtWidgets.QLineEdit(self.dockWidgetContents_10)
        self.lineEdit_Pwd.setGeometry(QtCore.QRect(140, 110, 111, 31))
        self.lineEdit_Pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_Pwd.setObjectName("lineEdit_Pwd")
        self.dockWidget_Server.setWidget(self.dockWidgetContents_10)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_Server)
        self.dockWidgetOutput = QtWidgets.QDockWidget(MainWindow)
        self.dockWidgetOutput.setObjectName("dockWidgetOutput")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.textEdit_ConnectStatus = QtWidgets.QTextEdit(self.dockWidgetContents)
        self.textEdit_ConnectStatus.setGeometry(QtCore.QRect(0, 0, 271, 262))
        self.textEdit_ConnectStatus.setMinimumSize(QtCore.QSize(0, 231))
        self.textEdit_ConnectStatus.setStyleSheet("QDockWidget > QWidget {\n"
"    border: 1px solid black;\n"
"}")
        self.textEdit_ConnectStatus.setObjectName("textEdit_ConnectStatus")
        self.dockWidgetOutput.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetOutput)
        self.actionopen = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/icons8-send-file-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionopen.setIcon(icon3)
        self.actionopen.setObjectName("actionopen")
        self.actionconnectServer = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/icons8-cloud-link-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionconnectServer.setIcon(icon4)
        self.actionconnectServer.setObjectName("actionconnectServer")
        self.actioncolseServer = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/icons8-cloud-cross-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actioncolseServer.setIcon(icon5)
        self.actioncolseServer.setObjectName("actioncolseServer")
        self.toolBar.addAction(self.actionopen)
        self.toolBar.addAction(self.actionconnectServer)
        self.toolBar.addAction(self.actioncolseServer)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rot-Device Diagnosis"))
        self.dockWidget_10.setWindowTitle(_translate("MainWindow", "Figure"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.dockWidget_Parameter.setWindowTitle(_translate("MainWindow", "Parameters"))
        self.label_Visualization.setText(_translate("MainWindow", "Visualization"))
        self.label_KMeans.setText(_translate("MainWindow", "K-Means:"))
        self.label_GaussianMixture.setText(_translate("MainWindow", "Gaussian Mixture:"))
        self.radioButton_k.setText(_translate("MainWindow", "K"))
        self.radioButton_Sample.setText(_translate("MainWindow", "Sample"))
        self.radioButton_k_2.setText(_translate("MainWindow", "K"))
        self.radioButton_Sample_2.setText(_translate("MainWindow", "Sample"))
        self.label_MeanShift.setText(_translate("MainWindow", "Mean-Shift:"))
        self.radioButton_Sample_3.setText(_translate("MainWindow", "Sample"))
        self.dockWidget_Server.setWindowTitle(_translate("MainWindow", "Server"))
        self.label_IP.setText(_translate("MainWindow", "IP Address"))
        self.label_PORT.setText(_translate("MainWindow", "PORT"))
        self.pushButton_Upload.setText(_translate("MainWindow", " Upload"))
        self.pushButton_Download.setText(_translate("MainWindow", " Download"))
        self.label_User.setText(_translate("MainWindow", "USER"))
        self.label_User_2.setText(_translate("MainWindow", "Password"))
        self.dockWidgetOutput.setWindowTitle(_translate("MainWindow", "Output"))
        self.actionopen.setText(_translate("MainWindow", "openfiles"))
        self.actionconnectServer.setText(_translate("MainWindow", "connectServer"))
        self.actioncolseServer.setText(_translate("MainWindow", "colseServer"))
        self.actioncolseServer.setToolTip(_translate("MainWindow", "colseServer"))