# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 4:25 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : config_utils.py
# @Software: PyCharm
import configparser
import os

current = os.path.dirname(__file__)
config_path = os.path.join(current, '../Config/config.ini')


class ConfigUtils:

    def __init__(self, path=config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(path, encoding="utf-8")

    @property
    def get_url(self):
        url = self.cfg.get("DEFAULT", "LOGIN_URL")
        return url

    @property
    def get_driver_path(self):
        url = self.cfg.get("DRIVER_PATH", "DRIVER_PATH")
        return url

    @property
    def get_screen_shot_path(self):
        url = self.cfg.get("SCREEN", "SCREEN_PATH")
        return url

    @property
    def log_path(self):
        logs_path = self.cfg.get("LOGS", "LOGS_PATH")
        return logs_path

    @property
    def log_level(self):
        logs_level = self.cfg.get("LOGS", "LOG_LEVEL")
        return int(logs_level)





local_config = ConfigUtils()

if __name__ == "__main__":
    print(    local_config.get_screen_shot_path)