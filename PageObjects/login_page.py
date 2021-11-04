# -*- coding: utf-8 -*-
# @Time : 2021/11/4 15:44
# @Author : Limusen
# @File : login_page

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageLocators.login_locator import LoginLocators as loc


class LoginPage:

    def __init__(self, driver: WebDriver):
        # 属性 - 元素定位
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def login(self, name, password):
        self.wait.until(EC.visibility_of_element_located(loc.username_input_box))
        self.driver.find_element(*loc.username_input_box).send_keys(name)
        self.driver.find_element(*loc.password_input_box).send_keys(password)
        self.driver.find_element(*loc.login_button).click()

    def get_error_msg_from_login_area(self):
        """
        登录失败的时候，弹窗提示
        :return:
        """
        self.wait.until(EC.visibility_of_element_located(*loc.error_tip_from_login_area))
        return self.driver.find_element(*loc.error_tip_from_login_area).text
