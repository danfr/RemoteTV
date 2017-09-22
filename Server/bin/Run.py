import signal
import sys

from Server.bin.Server import Server
from Server.bin.Utils import Utils

config = Utils.load_configuration()
port = config['NETWORK']['PORT']

listener = Server()
listener.start()


def signal_handler(signal, frame):
    print('Server shutting down !')
    listener.stop()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
