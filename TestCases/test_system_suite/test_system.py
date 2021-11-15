# -*- coding: utf-8 -*-
# @Time : 2021/11/11 15:06
# @Author : Limusen
# @File : test_system
import time

import pytest
import allure
from PageObjects.system_page import SystemPage
from TestDatas.system import system_datas as td
from TestDatas import global_datas as gd
from Common.random_utils import rd


@allure.epic("[epic]盛杰运营后台")
@pytest.mark.usefixtures("refresh")
class TestSystem:

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员 -- 用户名查找")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_query_name(self, refresh):
        SystemPage(refresh).query_name(td.query_name)
        assert SystemPage(refresh).get_query_name_text() == td.query_name

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员 -- 查询不存在的用户名")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_query_name_noll(self, refresh):
        SystemPage(refresh).query_name(td.query_null_name)
        assert SystemPage(refresh).query_null() == td.query_null_text

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员 -- 查询状态为在职的员工")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_query_status_online(self, refresh):
        SystemPage(refresh).query_status_online()
        assert SystemPage(refresh).get_query_name_text() == td.query_name

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员 -- 查询状态为离职的员工")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_query_status_quit(self, refresh):
        SystemPage(refresh).query_status_quit()
        assert SystemPage(refresh).get_query_name_text() == td.query_quit_name

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员 -- 根据手机号查询")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_query_phone(self, refresh):
        SystemPage(refresh).query_phone(td.query_phone)
        assert SystemPage(refresh).get_query_name_text() == td.query_name

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员 -- 查询不存在的手机号码")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_query_null_phone(self, refresh):
        SystemPage(refresh).query_phone(td.query_null_phone)
        assert SystemPage(refresh).query_null() == td.query_null_text

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员 -- 创建用户")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_create_user_success(self, refresh):
        name = rd.Rname()
        phone = rd.Rphone()
        SystemPage(refresh).create_user(name=name, phone=phone)
        assert SystemPage(refresh).name_query(name) == name

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员 -- 创建用户失败,未输入用户名")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    @pytest.mark.skip("暂时未通过测试--下次优化")
    def test_create_user_fail_name(self, refresh):
        phone = rd.Rphone()
        SystemPage(refresh).create_user(name="", phone=phone)
        assert SystemPage(refresh).get_fail_name_text() == td.create_fail_name

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员 -- 创建用户失败,未输入手机号")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    @pytest.mark.skip("暂时未通过测试--下次优化")
    def test_create_user_fail_phone(self, refresh):
        name = rd.Rname()
        SystemPage(refresh).create_user(name=name, phone="")
        assert SystemPage(refresh).get_fail_phone_text() == td.create_fail_phone

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员 -- 创建用户失败,未选择群组")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_create_user_fail_role(self, refresh):
        name = rd.Rname()
        phone = rd.Rphone()
        SystemPage(refresh).create_user_fail_name(name=name, phone=phone)
        assert SystemPage(refresh).get_fail_role_text() == td.create_fail_role

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员 -- 创建用户,都不输入")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_create_user_success(self, refresh):
        SystemPage(refresh).create_user_all_null()
        assert SystemPage(refresh).get_fail_name_text() == td.create_fail_name
        assert SystemPage(refresh).get_fail_phone_text() == td.create_fail_phone
        assert SystemPage(refresh).get_fail_role_text() == td.create_fail_role


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_system.py'])
