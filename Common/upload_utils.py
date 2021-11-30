# -*- coding: utf-8 -*-
# @Time : 2021/11/30 14:24
# @Author : Limusen
# @File : upload_utils


import os
import sys
import time
import pyperclip
import pyautogui
from sys import platform as plat
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from pywinauto.keyboard import send_keys
from selenium.webdriver.chrome.webdriver import WebDriver
from Common.log_utils import logger
from Common.config_utils import local_config
from Common.base_page import BasePage

system = sys.platform


class UploadUtils(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_file_path(self, filepath):  # /testFile/1.xlsx
        """
        获取文件路径
        :param filepath: 将需要获取的地址写入
        :return: 返回给upload_file_mac使用
        """
        # 获取上一级路径
        up_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # 拼接filepath
        add_path = os.path.join(up_path, filepath)
        return add_path

    def upload_win_auto_gui(self, text, page_action):
        """
        :param text: 输入的路径
        :return:
        :decriprtion: 只适用于windows 且不需要获取上层目录路径,只需要传入具体的文件路径
        :ex: os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'file\test1.mp4')
        """
        try:
            self.wait(3)
            # 输入文件
            send_keys(text)
            self.wait(1)
            send_keys('{VK_RETURN}')
        except Exception as e:
            logger.error("当前脚本不能执行原因是: %s" % e)
            self.get_page_img(page_action)

    def upload(self, **kwargs):
        """优化上传文件 windows与mac系统上传文件分开上传"""
        if plat == "win32":
            self.__upload_file(file_path=kwargs["file_path"], page_action=kwargs['page_action'])
        elif plat == "darwin":
            self.__upload_file_mac(file_path=kwargs["file_path"], page_action=kwargs['page_action'])

    def upload_file_path(self, text, page_action):
        """
        新增上传文件的方法,不用基于autoit方法
        :param text: 传入文本的路径
        :return:
        """
        try:
            self.wait(2)
            # 键盘操作输入路径
            pyautogui.write(text)
            # 输入键盘事件
            pyautogui.press('enter', 2)
        except Exception as e:
            logger.error("当前脚本不能执行原因是: %s" % e)
            self.get_page_img(page_action)

    def __upload_file(self, file_path, page_action, file_exe_path=local_config.get_upload_path, browser="chrome"):
        """上传文件"""
        try:
            """上传文件"""
            # 支持中文路径
            if sys.platform.lower() == 'win32':
                exe_file = file_exe_path
                cmd = "\"" + exe_file + "\"" + " " + "\"" + browser + "\"" + " " + "\"" + file_path + "\""
                cd = os.popen(cmd)
                self.wait(2)
                cd.close()
        except Exception as e:
            logger.error("当前脚本不能执行原因是: %s" % e)
            self.get_page_img(page_action)

    def __upload_file_mac(self, file_path, page_action):
        """
        :param file:  文件路径  mac上传文件方法
        :return:
        """
        try:
            time.sleep(1)
            k = PyKeyboard()
            m = PyMouse()
            filepathheard = '/'
            k.press_keys(['Command', 'Shift', 'G'])
            x_dim, y_dim = m.screen_size()
            m.click(x_dim // 2, y_dim // 2, 1)
            time.sleep(1)
            # 复制文件路径开头的斜杠/
            pyperclip.copy(filepathheard)
            time.sleep(1)
            # 粘贴斜杠/
            k.press_keys(['Command', 'V'])
            # 拼接完整路径
            time.sleep(1)
            fi = self.get_file_path(file_path)
            time.sleep(1)
            # 输入文件全路径进去
            k.type_string(fi)
            k.press_key('Return')
            time.sleep(2)
            k.press_key('Return')
            time.sleep(2)
        except Exception as e:
            logger.error("当前脚本不能执行原因是: %s" % e)
            self.get_page_img(page_action)
