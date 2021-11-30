# -*- coding: utf-8 -*-
# @Time : 2021/11/29 16:17
# @Author : Limusen
# @File : test_system_role_management


import pytest
import allure
from PageObjects.system_ob.system_role_page import SystemRolePage
from Common.random_utils import rd
from TestDatas.system import system_role_datas as td
from TestDatas import global_datas as gd


@allure.epic("[epic]盛杰运营后台")
@pytest.mark.usefixtures("refresh")
class TestSystemRoleManagement:

    @allure.story("[Story]系统管理-角色管理")
    @allure.title("[TiTile]case 新建角色 ")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_create_role(self, refresh):
        code = rd.Rcode()
        SystemRolePage(refresh).create_role(name=td.role_name, code=code)
        result = SystemRolePage(refresh).get_role_name()
        assert result == td.role_name

    @allure.story("[Story]系统管理-角色管理")
    @allure.title("[TiTile]case 新建角色 - 不输入用户名 ")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_create_role_fail_name(self, refresh):
        code = rd.Rcode()
        SystemRolePage(refresh).create_role(name="", code=code)
        assert SystemRolePage(refresh).get_error_no_name() == td.role_error_name

    @allure.story("[Story]系统管理-角色管理")
    @allure.title("[TiTile]case 新建角色 - 不输入编号 ")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_create_role_fail_code(self, refresh):
        SystemRolePage(refresh).create_role(name=td.role_name, code="")
        assert SystemRolePage(refresh).get_error_no_code() == td.role_error_code

    @allure.story("[Story]系统管理-角色管理")
    @allure.title("[TiTile]case 新建角色 - 不选择群组 ")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_create_role_fail_group(self, refresh):
        SystemRolePage(refresh).create_role_no_select_group(name=td.role_name, code="1024")
        assert SystemRolePage(refresh).get_error_no_group() == td.role_error_group

    @allure.story("[Story]系统管理-角色管理")
    @allure.title("[TiTile]case 查看群组用户 - 查看新建组为空组 ")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_view_group_no_data(self, refresh):
        SystemRolePage(refresh).view_user_role()
        assert SystemRolePage(refresh).get_no_data_message() == td.role_no_data

    @allure.story("[Story]系统管理-角色管理")
    @allure.title("[TiTile]case 修改群组权限 ")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_edit_group(self, refresh):
        SystemRolePage(refresh).edit_user_role()
        assert SystemRolePage(refresh).get_group_role_name() == td.role_group_name

    @allure.story("[Story]系统管理-角色管理")
    @allure.title("[TiTile]case 删除群组 ")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_edit_group(self, refresh):
        SystemRolePage(refresh).delete_group()
        assert SystemRolePage(refresh).get_role_name() != td.role_name


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_system_role_management.py'])
