import configparser
import os

class ReadConfig:
    """定义一个读取配置文件的类"""

    def __init__(self, filepath=None):
        if filepath:
            configpath = filepath
        else:
            root_dir = os.path.abspath('.')
            configpath = os.path.join(root_dir, "config.ini")

        print("configpath:"+configpath)

        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)

    def get_login_key(self, param):
        value = self.cf.get("Login", param)
        return value
