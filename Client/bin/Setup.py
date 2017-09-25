import os

from pathlib import Path


class Setup:
    CONFIGURATION_FILE = os.path.join(Path(__file__).parents[1], "config", "client.cfg")
    RED_LED = os.path.join(Path(__file__).parents[1], "view", "icons", "red-led-on.png")
    GREEN_LED = os.path.join(Path(__file__).parents[1], "view", "icons", "green-led-on.png")
