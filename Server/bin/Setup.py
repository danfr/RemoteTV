import os

from pathlib import Path


class Setup:
    CONFIGURATION_FILE = os.path.join(Path(__file__).parents[1], "config", "server.cfg")
    VLC_DEFAULT_COMMAND = "vlc -f"
