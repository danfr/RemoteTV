from subprocess import Popen, PIPE
from threading import Thread

from bin.Setup import Setup
from bin.Utils import Utils


class VLCStreamer:
    __attrs__ = ['file', 'port', 'current_streams']

    current_streams = {}

    def __init__(self, file, port):
        self.file = file
        self.port = port
        self.current_process = None

    @staticmethod
    def start_streaming(file, port):
        streamer = VLCStreamer(file, port)
        VLCStreamer.current_streams[port] = streamer
        streamer.start()

    def start(self):
        stream = Thread(target=self._stream, daemon=True)
        stream.start()

    def _stream(self):
        command = self._get_vlc_command()
        config = Utils.load_configuration()
        path = config["EXTERNAL"]["VLC_DIR"]
        self.current_process = Popen(command, stdout=PIPE, bufsize=1, close_fds=Setup.POSIX, shell=True, cwd=path)

    def _get_vlc_command(self):
        local_ip = Utils.get_lan_ip()
        command = Setup.VLC_COMMAND_PATTERN.replace("#FILE#", self.file, 1).replace("#STR_IP#", local_ip) \
            .replace("#STR_PORT#", str(self.port))
        return command
