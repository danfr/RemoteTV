import os
import sys
from pathlib import Path


class Setup:
    CONFIGURATION_FILE = os.path.join(Path(__file__).parents[1], "config", "server.cfg")
    VLC_DEFAULT_COMMAND = "vlc -f"
    POSIX = 'posix' in sys.builtin_module_names
    VLC_PLAYLIST_END = "vlc://quit"
