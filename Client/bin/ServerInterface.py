import sys

import requests
from requests.exceptions import ConnectionError

from bin.Utils import Singleton, Utils


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
