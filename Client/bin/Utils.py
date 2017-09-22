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


class Singleton:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwds):
        if self.instance is None:
            self.instance = self.klass(*args, **kwds)
        return self.instance
