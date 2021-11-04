# -*- coding: utf-8 -*-
# @Time : 2021/11/4 16:20
# @Author : Limusen
# @File : home_page
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.home_locator import HomeLocator as loc


class HomePage:

    def __init__(self, driver: WebDriver):
        # 属性 - 元素定位
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def is_exit_exist(self):
        """
        如果存在,则返回True,如果不存在,则返回False
        :return:
        """
        try:
            self.wait.until(EC.visibility_of_element_located(loc.exit_loc))
        except:
            return False
        else:
            return True
