# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 4:38 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : browser.py
# @Software: PyCharm

import os
import sys
from selenium import webdriver
from Common.config_utils import local_config
from selenium.webdriver.chrome.options import Options
from Common.log_utils import logger
import warnings

# 浏览器类，用来提供driver驱动

current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path, "..", local_config.get_driver_path)

chrome_path = os.path.join(current_path, '..', 'Driver', 'chromedriver93.exe')

system_driver = sys.platform
class Browser:


    def __init__(self, path=driver_path):
        # 　去除控制台警告
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        self.driver_path = path
        self.driver_name = local_config.default_driver


    def get_driver(self):
        if self.driver_name.lower() == "chrome":
            logger.info("当前正在打开：%s" % self.driver_name)
            return self.__get_chrome_driver()
        elif self.driver_name.lower() == 'firefox':
            logger.info("当前正在打开：%s" % self.driver_name)
            return self.__get_firefox_driver()
        elif self.driver_name.lower() == "edge":
            logger.info("当前正在打开：%s" % self.driver_name)
            return self.__get_edge_driver()

    def __get_chrome_driver(self):
        # 先封装简易代码
        # 加入系统环境判断
        if system_driver.lower() == "darwin":
            chrome_options = Options()
            chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
            chrome_options.add_argument('lang=zh_CN.UTF-8')  # 设置默认编码为utf-8
            chrome_options.add_experimental_option('useAutomationExtension', False)  # 取消chrome受自动控制提示
            chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 取消chrome受自动控制提示
            """如果是mac系统执行这个驱动"""
            chrome_path = os.path.join(current_path, '..', 'Driver', 'chromedriver')
            driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
            return driver
        elif system_driver.lower() == "win32":
            chrome_options = Options()
            chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
            chrome_options.add_argument('lang=zh_CN.UTF-8')  # 设置默认编码为utf-8
            chrome_options.add_experimental_option('useAutomationExtension', False)  # 取消chrome受自动控制提示
            chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 取消chrome受自动控制提示
            chrome_path = os.path.join(current_path, '..', 'Driver', 'chromedriver93.exe')
            driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
            return driver
        elif system_driver.lower() == "linux":
            chrome_options = Options()
            chrome_options.add_argument('no-sandbox')
            chrome_options.add_argument("headless")  # => 为Chrome配置无头模式
            chrome_options.add_argument('disable-dev-shm-usage')
            chrome_options.add_argument('disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
            driver = webdriver.Chrome(options=chrome_options)
            return driver

    def __get_firefox_driver(self):
        if system_driver.lower() == "darwin":
            firefox_driver_path = os.path.join(self.driver_path, 'geckodriver')
            driver = webdriver.Firefox(executable_path=firefox_driver_path)
            logger.info('初始化Firefox浏览器并启动')
            return driver
        else:
            firefox_driver_path = os.path.join(self.driver_path, 'geckodriver.exe')
            driver = webdriver.Firefox(executable_path=firefox_driver_path)
            logger.info('初始化Firefox浏览器并启动')
            return driver

    def __get_edge_driver(self):
        edge_driver_path = os.path.join(self.driver_path, 'msedgedriver.exe')
        driver = webdriver.Edge(executable_path=edge_driver_path)
        logger.info('初始化Edge浏览器并启动')
        return driver

    def __get_remove_to_driver(self):  # selenium支持分布式 grid ==》配置（你自己的代码编写、对方电脑的配置）
        pass


if __name__ == "__main__":
    Browser().get_driver()
