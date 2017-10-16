from threading import Thread
from time import sleep

from PyQt5 import QtGui
from PyQt5.QtCore import QObject, QEvent
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from bin.Setup import Setup
from bin.Utils import Singleton
from view.MainWindow import Ui_MainWindow


@Singleton
class UIManager:
    __attrs__ = ['server', 'ui']

    def __init__(self, server, ui: Ui_MainWindow):
        self.server = server
        self.ui = ui
        self._filter = Filter(self)
        self.lock = False

    def initialize(self):
        server_watchdog = Thread(target=self._check_server_state, args=(self.server, self.ui), daemon=True)
        server_watchdog.start()
        self.ui.play_btn.clicked.connect(self._play_clicked)
        self.ui.play_stream_btn.clicked.connect(self._stream_clicked)
        self.ui.play_transfer_btn.clicked.connect(self._transfer_clicked)
        self.ui.file_path.installEventFilter(self._filter)

    def _check_server_state(self, server, window):
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

    def _play_clicked(self):
        source = self.ui.stream_url.text()
        if self.server.send_vlc_play_stream(source):
            self.ui.stream_url.setText("")

    def _stream_clicked(self):
        source = self.ui.file_path.text()
        if self.server.send_vlc_play_file(source):
            self.ui.file_path.setText("")

    def _transfer_clicked(self):
        source = self.ui.file_path.text()
        self.ui.statusBar.showMessage("Transferring file, please wait...")
        if self.server.send_vlc_send_file(source):
            self.ui.file_path.setText("")

    def _file_focused(self):
        if not self.lock:  # Avoid loop on focusIn event
            filename, _ = QFileDialog.getOpenFileName(QFileDialog(), "Select a file", "", "All Files (*)")
            if filename:
                if not Setup.POSIX:
                    self.ui.file_path.setText(filename.replace("/", "\\"))
                else:
                    self.ui.file_path.setText(filename)
            self.lock = True
        else:
            self.lock = False

    def showdialog(self, title, message, submessage="", icon=QMessageBox.Information, buttons=QMessageBox.Ok):
        msg = QMessageBox()
        msg.setIcon(icon)

        msg.setText(message)
        msg.setInformativeText(submessage)
        msg.setWindowTitle(title)
        msg.setStandardButtons(buttons)
        msg.setFixedWidth(500)

        return msg.exec_()


class Filter(QObject):
    def __init__(self, callback_class):
        super().__init__()
        self.callback_class = callback_class

    def eventFilter(self, widget, event):
        # FocusOut event
        if event.type() == QEvent.FocusIn:
            self.callback_class._file_focused()
            # return False so that the widget will also handle the event
            # otherwise it won't focus out
            return False
        else:
            # we don't care about other events
            return False
