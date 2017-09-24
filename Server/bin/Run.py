import signal
import sys

from bin.Server import Server
from bin.Utils import Utils

config = Utils.load_configuration()
port = int(config['NETWORK']['PORT'])

listener = Server()
listener.start(port)


def signal_handler(signal, frame):
    print('Server shutting down !')
    listener.stop()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
