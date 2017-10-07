import os
import sys
from pathlib import Path
from subprocess import Popen, PIPE
from threading import Thread
from time import sleep

from bin.Setup import Setup
from bin.Utils import Utils, Singleton


@Singleton
class Worker:
    current_process = None
    tmp_files = []

    def manage_command(self, form):
        try:
            command = form.getvalue('COMMAND')
        except KeyError:
            print("ERROR : No command given", file=sys.stderr)
            return 400

        try:
            if command == "PLAY_NEW_STREAM":
                return self.play_new_stream(form)
            elif command == "PLAY_NEW_FILE":
                return self.play_new_file(form)
            elif command == "PING":
                return 200
            elif command == "PROCESS_STATUS":
                return 102 if self.process_running() else 100
            else:
                return 405
        except KeyError as e:
            print("ERROR : Missing parameter(s) : ", e, file=sys.stderr)
            return 400
        except RuntimeError as e:
            print(e, file=sys.stderr)
            return 409

    def play_new_stream(self, form):
        source = form.getvalue('STREAM_SOURCE')
        if source is None:
            raise KeyError("STREAM_SOURCE")

        self.play_single_on_vlc(source)

        return 200

    def play_single_on_vlc(self, source):
        if not self.process_running():
            vlc = Utils.get_vlc_default()
            vlc_path = vlc[0]
            vlc_cmd = vlc[1] + ' "' + source + '" ' + Setup.VLC_PLAYLIST_END
            self.execute(vlc_cmd, vlc_path)
        else:
            raise RuntimeError("Process already running")

    def play_new_file(self, form):
        filename = os.path.join(Path(__file__).parents[1], "tmp", form.getvalue("FILENAME"))
        length = int(form.headers['Content-Length'])
        toto = form['FILE'].file
        with open(filename, 'wb+') as f:
            f.write(form['FILE'].file.read(length))

        self.tmp_files.append(filename)
        self.play_single_on_vlc(filename)
        return 200

    def execute(self, cmd, path):
        self.current_process = Popen(cmd, stdout=PIPE, bufsize=1, close_fds=Setup.POSIX, shell=True, cwd=path)
        process_watchdog = Thread(target=self._process_end, daemon=True)
        process_watchdog.start()

    def process_running(self):
        if self.current_process is None:
            return False

        if self.current_process.poll() is None:
            return True
        else:
            self.current_process = None
            return False

    def _process_end(self):
        while self.process_running():
            sleep(60)
        while self.tmp_files:
            file = self.tmp_files.pop()
            if os.path.isfile(file):
                os.remove(file)
