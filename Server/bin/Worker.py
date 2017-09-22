import sys
from subprocess import Popen, PIPE

from bin.Utils import Utils, Singleton


@Singleton
class Worker:
    current_process = None

    def manage_command(self, form):
        try:
            command = form['COMMAND']
        except KeyError:
            print("ERROR : No command given", file=sys.stderr)
            return 400

        try:
            if command == "PLAY_NEW_STREAM":
                source = form['SOURCE']
                self.play_new_stream(source)
                return 200
            else:
                return 405
        except KeyError:
            print("ERROR : Missing parameters", file=sys.stderr)
            return 400
        except RuntimeError as e:
            print(e, file=sys.stderr)
            return 409

    def play_new_stream(self, source):
        if not self.process_running():
            vlc = Utils.get_vlc_default()
            vlc_path = vlc[0]
            vlc_cmd = vlc[1] + " " + source
            self.execute(vlc_cmd, vlc_path)
        else:
            raise RuntimeError("Process already running")

    def execute(self, cmd, path):
        unix = 'posix' in sys.builtin_module_names
        self.current_process = Popen(cmd, stdout=PIPE, bufsize=1, close_fds=unix, shell=True, cwd=path)

    def process_running(self):
        if self.current_process is None:
            return False

        if self.current_process.poll() is None:
            return True
        else:
            self.current_process = None
            return False
