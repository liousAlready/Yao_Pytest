# -*- coding: utf-8 -*-
# @Time : 2021/11/4 15:44
# @Author : Limusen
# @File : test_login

import pytest
import allure
from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage
from TestDatas import login_datas as td

"""

前置
测试数据: 


"""


@allure.epic("[epic]盛杰运营后台")
@pytest.mark.usefixtures("refresh")
class TestLogin:

    # 　逆向场景　登录失败　数据格式无效
    @allure.story("[Story]用户根据用户名密码登录系统")
    @allure.title("[TiTile]case 异常用例")
    @allure.description("登录测试用例 执行人：李某")
    @pytest.mark.parametrize("case", td.invalid_data)
    def test_login_failed_invalid_data(self, case, refresh):
        LoginPage(refresh).login(case['user'], case['passwd'])
        assert LoginPage(refresh).get_error_msg_from_login_area() == case['check']

    # 正向场景 登录成功
    @allure.story("[Story]用户根据用户名密码登录系统")
    @allure.title("[TiTile]case 登录成功场景")
    @allure.description("登录测试用例 执行人：李某")
    @pytest.mark.smoker  # 执行冒烟
    def test_login_success(self, refresh):
        # 登录 --  步骤
        # 　调用登录页面的登录方法
        LoginPage(refresh).login(*td.valid_user)
        # 断言 --  首页是否存在运营后台元素
        assert HomePage(refresh).is_exit_exist()


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_login.py'])
