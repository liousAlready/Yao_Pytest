# -*- coding: utf-8 -*-
# @Time : 2021/11/4 15:44
# @Author : Limusen
# @File : test_login

import pytest
from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage
from TestDatas import login_datas as td

"""

前置
测试数据: 


"""


@pytest.mark.usefixtures("init")
class TestLogin:

    # 正向场景 登录成功
    def test_login_success(self, init):
        # 登录 --  步骤
        # 　调用登录页面的登录方法
        LoginPage(init).login(*td.valid_user)
        # 断言 --  首页是否存在运营后台元素
        assert HomePage(init).is_exit_exist()

    # 　逆向场景　登录失败　数据格式无效
    @pytest.mark.parametrize("case", td.invalid_data)
    def test_login_failed_invalid_data(self, case, init):
        LoginPage(init).login(case['user'], case['passwd'])
        assert LoginPage(init).get_error_msg_from_login_area() == case['check']


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_login.py'])
