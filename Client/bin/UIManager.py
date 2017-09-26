from threading import Thread
from time import sleep

from PyQt5 import QtGui

from bin.Setup import Setup
from bin.Utils import Singleton
from view.MainWindow import Ui_MainWindow


@Singleton
class UIManager:
    __attrs__ = ['server', 'ui']

    def __init__(self, server, ui: Ui_MainWindow):
        self.server = server
        self.ui = ui

    def initialize(self):
        server_watchdog = Thread(target=self.check_server_state, args=(self.server, self.ui), daemon=True)
        server_watchdog.start()
        self.ui.play_btn.clicked.connect(self.play_clicked)

    def check_server_state(self, server, window):
        """THREAD USE ONLY !"""
        while True:
            if server.ping():
                window.widget_server_status.setPixmap(QtGui.QPixmap(Setup.GREEN_LED))
                window.widget_server_status.setToolTip("Server connected")
                server.active = True

                if server.is_process_running():
                    window.statusBar.showMessage("Playing on remote...")
                else:
                    window.statusBar.showMessage("")
            else:
                window.widget_server_status.setPixmap(QtGui.QPixmap(Setup.RED_LED))
                window.widget_server_status.setToolTip("Server unreachable")
                server.active = False

            sleep(5)

    def play_clicked(self):
        source = self.ui.stream_url.text()
        self.server.send_vlc_play_stream(source)
