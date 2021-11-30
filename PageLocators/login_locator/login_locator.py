# -*- coding: utf-8 -*-
# @Time : 2021/11/4 15:39
# @Author : Limusen
# @File : login_page

from selenium.webdriver.common.by import By


class LoginLocators:
    # 用户名输入框
    username_input_box = (By.XPATH, '//*[@placeholder="请输入账号"]')
    # 密码输入框
    password_input_box = (By.XPATH, '//*[@placeholder="请输入密码"]')
    # 登录按钮
    login_button = (By.XPATH, '//*[@type="button"]')
    # 短信登录按钮
    message_button = (By.XPATH, '//*[@class="item"]')
    # 手机号输入框
    phone_input_box = (By.XPATH, '//*/*[@type="phone"]')
    # 点击发送验证码
    message_click = (By.XPATH, '//*/*[@class="button_verification"]')
    # 登录按钮
    message_login_button = (By.XPATH, '//*/*[@class="button_login"]')
    # 用户名密码错误提示
    error_tip_from_login_area = (By.XPATH, '//*[@class="el-message el-message--error"]')
    # 用户不存在
    account_non_existent = (By.XPATH, '//*[@class="el-message el-message--error"]')
