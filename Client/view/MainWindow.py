# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
import ctypes
import os
from pathlib import Path

from PyQt5 import QtCore, QtGui, QtWidgets

from bin.Setup import Setup
from bin.Utils import Singleton


@Singleton
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not Setup.POSIX:
            myappid = '75a57eb5-5a4f-427a-96ae-bdf0a959fba1'  # arbitrary string
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 400)
        app_icon = QtGui.QIcon()
        app_icon.addFile(Setup.ICON16, QtCore.QSize(16, 16))
        app_icon.addFile(Setup.ICON24, QtCore.QSize(24, 24))
        app_icon.addFile(Setup.ICON32, QtCore.QSize(32, 32))
        app_icon.addFile(Setup.ICON48, QtCore.QSize(48, 48))
        app_icon.addFile(Setup.ICON256, QtCore.QSize(256, 256))
        MainWindow.setWindowIcon(app_icon)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(245, 400))
        MainWindow.setMaximumSize(QtCore.QSize(250, 400))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.server_url = QtWidgets.QLabel(self.centralwidget)
        self.server_url.setGeometry(QtCore.QRect(0, 30, 250, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.server_url.setFont(font)
        self.server_url.setAlignment(QtCore.Qt.AlignCenter)
        self.server_url.setObjectName("server_url")

        # Custom LED Widget
        self.widget_server_status = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.widget_server_status.setFont(font)
        self.widget_server_status.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.widget_server_status.setText("toto")
        path = os.path.join(Path(__file__).parent, "icons", "red-led-on.png")
        self.widget_server_status.setPixmap(QtGui.QPixmap(path))
        self.widget_server_status.setScaledContents(True)
        self.widget_server_status.setGeometry(QtCore.QRect(105, 65, 40, 40))
        self.widget_server_status.setObjectName("widget_server_status")

        self.label_server_url = QtWidgets.QLabel(self.centralwidget)
        self.label_server_url.setGeometry(QtCore.QRect(98, 10, 54, 16))
        self.label_server_url.setObjectName("label_server_url")
        MainWindow.setCentralWidget(self.centralwidget)

        self.label_stream_url = QtWidgets.QLabel(self.centralwidget)
        self.label_stream_url.setGeometry(QtCore.QRect(70, 120, 110, 16))
        self.label_stream_url.setObjectName("label_stream_url")
        self.stream_url = QtWidgets.QLineEdit(self.centralwidget)
        self.stream_url.setGeometry(QtCore.QRect(20, 150, 210, 20))
        self.stream_url.setObjectName("stream_url")
        self.play_btn = QtWidgets.QPushButton(self.centralwidget)
        self.play_btn.setGeometry(QtCore.QRect(90, 185, 70, 23))
        self.play_btn.setObjectName("play_btn")
        self.label_file_path = QtWidgets.QLabel(self.centralwidget)
        self.label_file_path.setGeometry(QtCore.QRect(85, 230, 110, 16))
        self.label_file_path.setObjectName("label_file_path")
        self.file_path = QtWidgets.QLineEdit(self.centralwidget)
        self.file_path.setGeometry(QtCore.QRect(20, 260, 210, 20))
        self.file_path.setObjectName("file_path")
        self.play_stream_btn = QtWidgets.QPushButton(self.centralwidget)
        self.play_stream_btn.setGeometry(QtCore.QRect(75, 295, 100, 23))
        self.play_stream_btn.setObjectName("play_stream_btn")
        self.play_transfer_btn = QtWidgets.QPushButton(self.centralwidget)
        self.play_transfer_btn.setGeometry(QtCore.QRect(75, 320, 100, 23))
        self.play_transfer_btn.setObjectName("play_transfer_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RemoteTV"))
        self.server_url.setText(_translate("MainWindow", "TextLabel"))
        self.label_server_url.setText(_translate("MainWindow", "Server URL"))
        self.label_stream_url.setText(_translate("MainWindow", "Paste stream URL here"))
        self.label_file_path.setText(_translate("MainWindow", "Choose local file"))
        self.play_btn.setText(_translate("MainWindow", "Play"))
        self.play_stream_btn.setText(_translate("MainWindow", "Stream and play"))
        self.play_transfer_btn.setText(_translate("MainWindow", "Transfer and play"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
