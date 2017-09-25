import sys
from threading import Thread
from time import sleep

from PyQt5 import QtWidgets, QtGui

from bin.ServerInterface import ServerInterface
from bin.Setup import Setup
from bin.Utils import Utils
from view.MainWindow import Ui_MainWindow


def check_server_state(server, window):
    """THREAD USE ONLY !"""
    while True:
        if server.ping():
            window.widget_server_status.setPixmap(QtGui.QPixmap(Setup.GREEN_LED))
            window.widget_server_status.setToolTip("Server connected")
            server.active = True
        else:
            window.widget_server_status.setPixmap(QtGui.QPixmap(Setup.RED_LED))
            window.widget_server_status.setToolTip("Server unreachable")
            server.active = False
        sleep(5)


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

config = Utils.load_configuration()
ui.server_url.setText(config["SERVER"]["URL"])

serv = ServerInterface()
server_watchdog = Thread(target=check_server_state, args=(serv, ui), daemon=True)
server_watchdog.start()

# serv.send_vlc_play_stream("https://www.youtube.com/watch?v=QH2-TGUlwu4")
sys.exit(app.exec_())
