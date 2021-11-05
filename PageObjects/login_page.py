# -*- coding: utf-8 -*-
# @Time : 2021/11/4 15:44
# @Author : Limusen
# @File : login_page

from PageLocators.login_locator import LoginLocators as loc
from Common.base_page import BasePage


class LoginPage(BasePage):

    def login(self, name, password):
        # self.wait.until(EC.visibility_of_element_located(loc.username_input_box))
        # self.driver.implicitly_wait(10)
        # self.driver.find_element(*loc.username_input_box).send_keys(name)
        # self.driver.find_element(*loc.password_input_box).send_keys(password)
        # self.driver.find_element(*loc.login_button).click()

        self.input_text(loc.username_input_box, "登录页面-输入用户名", name)
        self.input_text(loc.password_input_box, "登录页面-输入密码", password)
        self.click(loc.login_button,"登录页面-点击登录按钮")

    def get_error_msg_from_login_area(self):
        """
        登录失败的时候，弹窗提示
        :return:
        """
        return self.get_text(loc.error_tip_from_login_area, "登录页面-获取登录区域错误提示信息")
