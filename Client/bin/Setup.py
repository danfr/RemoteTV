import os
import sys
from pathlib import Path


class Setup:
    CONFIGURATION_FILE = os.path.join(Path(__file__).parents[1], "config", "client.cfg")
    RED_LED = os.path.join(Path(__file__).parents[1], "view", "icons", "red-led-on.png")
    GREEN_LED = os.path.join(Path(__file__).parents[1], "view", "icons", "green-led-on.png")
    POSIX = 'posix' in sys.builtin_module_names
    VLC_COMMAND_PATTERN = 'vlc -vvv "#FILE#" --sout "#http{mux=ffmpeg{mux=flv},dst=#STR_IP#:#STR_PORT#}" --intf dummy --network-caching 2000 --live-caching 2000 --ttl 5  --file-caching=5000'
