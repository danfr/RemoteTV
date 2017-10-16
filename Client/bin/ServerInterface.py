import os
import sys

import requests
from PyQt5.QtWidgets import QMessageBox
from requests.exceptions import ConnectionError

from bin.Setup import Setup
from bin.UIManager import UIManager
from bin.Utils import Singleton, Utils
from bin.VLCStreamer import VLCStreamer


@Singleton
class ServerInterface:
    __attrs__ = ['server_url', 'active']

    def __init__(self):
        conf = Utils.load_configuration()
        self.server_url = conf["SERVER"]["URL"]
        self.active = False

    def send_vlc_play_stream(self, source):
        """Send already exiting stream (eg: youtube) to remote"""
        # data to be sent
        data = {'COMMAND': "PLAY_NEW_STREAM",
                'STREAM_SOURCE': source}

        # sending post request and saving response as response object
        try:
            r = requests.post(url=self.server_url, data=data)
        except ConnectionError as e:
            print("ERROR : Server unavailable at " + self.server_url, e, file=sys.stderr)
            return False

        return r.status_code == 200

    def send_vlc_play_file(self, file):
        """Create a new stream from a local file and send it to remote"""
        ip = Utils.get_lan_ip()
        port = Utils.get_free_tcp_port()
        VLCStreamer.start_streaming(file, port)
        source = "http://" + ip + ":" + str(port)

        # data to be sent
        data = {'COMMAND': "PLAY_NEW_STREAM",
                'STREAM_SOURCE': source}

        # sending post request and saving response as response object
        try:
            r = requests.post(url=self.server_url, data=data)
        except ConnectionError as e:
            print("ERROR : Server unavailable at " + self.server_url, e, file=sys.stderr)
            return False

        return r.status_code == 200

    def send_vlc_send_file(self, file):
        """Send a local file to remote"""
        # Check input
        if not os.path.isfile(file):
            uim = UIManager()
            uim.showdialog("Bad input", "The given path is not a file :", file, icon=QMessageBox.Warning)
            return False
        else:
            _, file_extension = os.path.splitext(file)
            if file_extension not in Setup.SUPPORTED_EXT:
                uim = UIManager()
                uim.showdialog("Bad input", "The given file type is not supported", file, icon=QMessageBox.Warning)
                return False

        # data to be sent
        filename = os.path.basename(file)
        data = {'COMMAND': "PLAY_NEW_FILE",
                'FILENAME': filename}

        # sending post request and saving response as response object
        try:
            with open(file, 'rb') as f:
                r = requests.post(url=self.server_url, data=data, files={"FILE": ("binaryfile", f)})
        except ConnectionError as e:
            print("ERROR : Server unavailable at " + self.server_url, e, file=sys.stderr)
            return False

        return r.status_code == 200

    def ping(self):
        """Check if server is still alive"""
        # data to be sent
        data = {'COMMAND': "PING"}

        # sending post request and saving response as response object
        try:
            r = requests.post(url=self.server_url, data=data)
        except ConnectionError as e:
            print("ERROR : Server unavailable at " + self.server_url, e, file=sys.stderr)
            return False

        return r.status_code == 200

    def is_process_running(self):
        """Check if a process is running on the remote"""
        # data to be sent
        data = {'COMMAND': "PROCESS_STATUS"}

        # sending post request and saving response as response object
        try:
            r = requests.post(url=self.server_url, data=data)
        except ConnectionError as e:
            print("ERROR : Server unavailable at " + self.server_url, e, file=sys.stderr)
            return False

        return r.status_code == 102
