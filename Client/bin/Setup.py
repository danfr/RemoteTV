import os
import sys
from pathlib import Path


class Setup:
    CONFIGURATION_FILE = os.path.join(Path(__file__).parents[1], "config", "client.cfg")
    RED_LED = os.path.join(Path(__file__).parents[1], "view", "icons", "red-led-on.png")
    GREEN_LED = os.path.join(Path(__file__).parents[1], "view", "icons", "green-led-on.png")
    ICON16 = os.path.join(Path(__file__).parents[1], "view", "icons", "icon-16.png")
    ICON24 = os.path.join(Path(__file__).parents[1], "view", "icons", "icon-24.png")
    ICON32 = os.path.join(Path(__file__).parents[1], "view", "icons", "icon-32.png")
    ICON48 = os.path.join(Path(__file__).parents[1], "view", "icons", "icon-48.png")
    ICON256 = os.path.join(Path(__file__).parents[1], "view", "icons", "icon-256.png")
    SUPPORTED_EXT = [".mp4", ".avi"]
    POSIX = 'posix' in sys.builtin_module_names
    VLC_COMMAND_PATTERN = 'vlc -vvv "#FILE#" --sout "#http{mux=ffmpeg{mux=flv},dst=#STR_IP#:#STR_PORT#}" --intf null --network-caching 2000 --live-caching 2000 --ttl 5 --file-caching=5000 --play-and-exit'
