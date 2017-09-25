import configparser
import os
from time import sleep

from PyQt5 import QtGui

from bin.Setup import Setup


class Utils:
    @staticmethod
    def load_configuration():
        file = Setup.CONFIGURATION_FILE
        if os.path.isfile(file):
            config = configparser.ConfigParser()
            config.read(file)
        else:
            raise FileNotFoundError("Configuration file not found at : " + file)
        return config

    @staticmethod
    def set_server_state(serv, ui):
        """THREAD USE ONLY !"""
        while True:
            if serv.ping():
                ui.widget_server_status.setPixmap(QtGui.QPixmap(Setup.GREEN_LED))
                ui.widget_server_status.setToolTip("Server connected")
            else:
                ui.widget_server_status.setPixmap(QtGui.QPixmap(Setup.RED_LED))
                ui.widget_server_status.setToolTip("Server unreachable")
            sleep(5)


class Singleton:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwds):
        if self.instance is None:
            self.instance = self.klass(*args, **kwds)
        return self.instance

