import os
import sys

import requests
from requests.exceptions import ConnectionError

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

    def send_vlc_send_file(self, file):
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

    def ping(self):
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
        # data to be sent
        data = {'COMMAND': "PROCESS_STATUS"}

        # sending post request and saving response as response object
        try:
            r = requests.post(url=self.server_url, data=data)
        except ConnectionError as e:
            print("ERROR : Server unavailable at " + self.server_url, e, file=sys.stderr)
            return False

        return r.status_code == 102
