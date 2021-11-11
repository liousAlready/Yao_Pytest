# -*- coding: utf-8 -*-
# @Time : 2021/11/11 15:06
# @Author : Limusen
# @File : test_system


import pytest
import allure
from PageObjects.system_page import SystemPage
from TestDatas.system import system_datas as td
from TestDatas import global_datas as gd


@allure.epic("[epic]盛杰运营后台")
@pytest.mark.usefixtures("refresh")
class TestSystem:

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员--用户名查找")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_query_name(self, refresh):
        SystemPage(refresh).query_name(td.query_name)
        assert SystemPage(refresh).get_query_name_text() == td.query_name

    @allure.story("[Story]系统管理-内部人员管理")
    @allure.title("[TiTile] case 查询内部人员--查询不存在的用户名")
    @allure.description("登录测试用例 执行人：{}".format(gd.executor))
    def test_query_name_noll(self, refresh):
        SystemPage(refresh).query_name(td.query_null_name)
        assert SystemPage(refresh).query_null() == "暂无数据"


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_system.py'])
