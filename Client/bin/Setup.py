import os

from pathlib import Path


class Setup:
    CONFIGURATION_FILE = os.path.join(Path(__file__).parents[1], "config", "client.cfg")
