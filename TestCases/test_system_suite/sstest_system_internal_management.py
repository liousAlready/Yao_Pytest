# -*- coding: utf-8 -*-
# @Time : 2021/11/11 15:06
# @Author : Limusen
# @File : test_system

import pytest
import allure
from PageObjects.system_ob.system_internal_page import SystemPage
from TestDatas.system import system_datas as td
from TestDatas import global_datas as gd
from Common.random_utils import rd


@allure.epic("[epic]盛杰运营后台")
@pytest.mark.usefixtures("refresh")
class TestSystemInternalManagement:

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员 -- 用户名查找")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_001_query_name(self, refresh):
        SystemPage(refresh).query_name(td.query_name)
        assert SystemPage(refresh).get_query_name_text() == td.query_name

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员 -- 查询不存在的用户名")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_002_query_name_noll(self, refresh):
        SystemPage(refresh).query_name(td.query_null_name)
        assert SystemPage(refresh).query_null() == td.query_null_text

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员 -- 查询状态为在职的员工")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_003_query_status_online(self, refresh):
        SystemPage(refresh).query_status_online()
        assert SystemPage(refresh).get_query_name_text() == td.query_name

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员 -- 查询状态为离职的员工")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_004_query_status_quit(self, refresh):
        SystemPage(refresh).query_status_quit()
        assert SystemPage(refresh).get_query_name_text() == td.query_quit_name

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员 -- 根据手机号查询")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_005_query_phone(self, refresh):
        SystemPage(refresh).query_phone(td.query_phone)
        assert SystemPage(refresh).get_query_name_text() == td.query_name

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员 -- 查询不存在的手机号码")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_006_query_null_phone(self, refresh):
        SystemPage(refresh).query_phone(td.query_null_phone)
        assert SystemPage(refresh).query_null() == td.query_null_text

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员 -- 创建用户")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_007_create_user_success(self, refresh):
        name = rd.Rname()
        phone = rd.Rphone()
        SystemPage(refresh).create_user(name=name, phone=phone)
        assert SystemPage(refresh).name_query(name) == name

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员 -- 创建用户失败,未输入用户名")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_008_create_user_fail_name(self, refresh):
        phone = rd.Rphone()
        SystemPage(refresh).create_user_no_query(name="", phone=phone)
        assert SystemPage(refresh).get_fail_name_text() == td.create_fail_name

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员 -- 创建用户失败,未输入手机号")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_009_create_user_fail_phone(self, refresh):
        name = rd.Rname()
        SystemPage(refresh).create_user_no_query(name=name, phone="")
        assert SystemPage(refresh).get_fail_phone_text() == td.create_fail_phone

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员 -- 创建用户失败,未选择群组")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_010_create_user_fail_role(self, refresh):
        name = rd.Rname()
        phone = rd.Rphone()
        SystemPage(refresh).create_user_fail_name(name=name, phone=phone)
        assert SystemPage(refresh).get_fail_role_text() == td.create_fail_role

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员 -- 创建用户,都不输入")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_011_create_user_success(self, refresh):
        SystemPage(refresh).create_user_all_null()
        assert SystemPage(refresh).get_fail_name_text() == td.create_fail_name
        assert SystemPage(refresh).get_fail_phone_text() == td.create_fail_phone
        assert SystemPage(refresh).get_fail_role_text() == td.create_fail_role

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员 -- 将新创建的用户修改到ui测试组")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_012_user_edit_success(self, refresh):
        SystemPage(refresh).edit_user_group()
        assert SystemPage(refresh).get_edit_group_message() == td.edit_message

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员 -- 将新创建的用户离职")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_013_user_quit_success(self, refresh):
        SystemPage(refresh).set_user_quit()
        assert SystemPage(refresh).get_quit_message() == td.quit_message


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'sstest_system_internal_management.py'])
