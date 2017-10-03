import configparser
import os
import socket

if os.name != "nt":
    import fcntl
    import struct

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
    def _get_interface_ip(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',
                                                                            ifname[:15]))[20:24])

    @staticmethod
    def get_lan_ip():
        ip = socket.gethostbyname(socket.gethostname())
        if ip.startswith("127.") and os.name != "nt":
            interfaces = [
                "eth0",
                "eth1",
                "eth2",
                "wlan0",
                "wlan1",
                "wifi0",
                "ath0",
                "ath1",
                "ppp0",
            ]
            for ifname in interfaces:
                try:
                    ip = Utils._get_interface_ip(ifname)
                    break
                except IOError:
                    pass
        return ip

    @staticmethod
    def get_free_tcp_port():
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp.bind(('', 0))
        addr, port = tcp.getsockname()
        tcp.close()

        return port


class Singleton:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwds):
        if self.instance is None:
            self.instance = self.klass(*args, **kwds)
        return self.instance

