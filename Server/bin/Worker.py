import sys
from subprocess import Popen, PIPE

from bin.Setup import Setup
from bin.Utils import Utils, Singleton


@Singleton
class Worker:
    current_process = None

    def manage_command(self, form):
        try:
            command = form.getvalue('COMMAND')
        except KeyError:
            print("ERROR : No command given", file=sys.stderr)
            return 400

        try:
            if command == "PLAY_NEW_STREAM":
                return self.play_new_stream(form)
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

        if not self.process_running():
            vlc = Utils.get_vlc_default()
            vlc_path = vlc[0]
            vlc_cmd = vlc[1] + " " + source
            self.execute(vlc_cmd, vlc_path)
        else:
            raise RuntimeError("Process already running")

        return 200

    def execute(self, cmd, path):
        self.current_process = Popen(cmd, stdout=PIPE, bufsize=1, close_fds=Setup.POSIX, shell=True, cwd=path)

    def process_running(self):
        if self.current_process is None:
            return False

        if self.current_process.poll() is None:
            return True
        else:
            self.current_process = None
            return False
