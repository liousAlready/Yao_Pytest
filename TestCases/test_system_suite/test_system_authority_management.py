# -*- coding: utf-8 -*-
# @Time : 2021/11/30 14:54
# @Author : Limusen
# @File : test_system_authority_management

import pytest
import allure
from PageObjects.system_ob.system_authority_page import SystemAuthorityPage
from TestDatas import global_datas as gd
from TestDatas.system import system_authorith_datas as td


@allure.epic("[epic]盛杰运营后台")
@pytest.mark.usefixtures("refresh")
class TestSystemAuthority:

    def test_success(self, refresh):
        SystemAuthorityPage(refresh).query_authority_name(td.query_name_text)
        assert SystemAuthorityPage(refresh).get_query_name() == td.query_name_text


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_system_authority_management.py'])
