# -*- coding: utf-8 -*-
# @Time : 2021/11/4 15:44
# @Author : Limusen
# @File : test_login

import pytest
from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage

"""

前置
测试数据: 


"""


@pytest.mark.usefixtures("init")
class TestLogin:

    def test_login_success(self, init):
        # 登录 --  步骤
        # 　调用登录页面的登录方法
        LoginPage(init).login("13252254992", "254992")
        # 断言 --  首页是否存在运营后台元素
        assert HomePage(init).is_exit_exist()

    def test_login_failed_no_user(self, init):
        # 登录 --  步骤
        # 　调用登录页面的登录方法
        LoginPage(init).login("", "254992")
        # 断言 --  首页是否存在运营后台元素
        assert LoginPage(init).get_error_msg_from_login_area() == "请输入手机号"

    def test_login_failed_no_password(self, init):
        # 登录 --  步骤
        # 　调用登录页面的登录方法
        LoginPage(init).login("13252254992", "")
        # 断言 --  首页是否存在运营后台元素
        assert LoginPage(init).get_error_msg_from_login_area() == "请输入密码"

    def test_login_failed_all_no(self, init):
        # 登录 --  步骤
        # 　调用登录页面的登录方法
        LoginPage(init).login("", "")
        # 断言 --  首页是否存在运营后台元素
        assert LoginPage(init).get_error_msg_from_login_area() == "请输入手机号"



if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_login.py'])
