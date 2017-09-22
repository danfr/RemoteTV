import configparser
import os

from bin.Setup import Setup


class Utils:
    @staticmethod
    def load_configuration():
        file = Setup.CONFIGURATION_FILE
        if os.path.isfile(file):
            config = configparser.ConfigParser()
            config.read(file)
        else:
            raise FileNotFoundError("Configuration file not found at : " + file)
        return config

    @staticmethod
    def get_vlc_default():
        config = Utils.load_configuration()
        vlc_bin_path = config['EXTERNAL']['VLC_DIR']
        vlc_cmd = Setup.VLC_DEFAULT_COMMAND
        return vlc_bin_path, vlc_cmd


class Singleton:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwds):
        if self.instance is None:
            self.instance = self.klass(*args, **kwds)
        return self.instance
