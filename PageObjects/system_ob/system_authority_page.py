# -*- coding: utf-8 -*-
# @Time : 2021/11/30 14:55
# @Author : Limusen
# @File : system_authority_page


from Common.base_page import BasePage
from PageLocators.system_locator.system_authority_locator import SystemAuthority as loc


class SystemAuthorityPage(BasePage):

    def click_two_button(self):
        self.click(loc.system_tab, "首页-点击系统管理tab")
        self.click(loc.authority_tab_button, "系统管理-点击权限管理tab")

    def query_authority_name(self, name):
        self.click_two_button()
        self.wait(1)
        self.input_text(loc.authority_input,"系统管理-查询权限名称" ,name)
        self.click(loc.authority_query_button, "系统管理-点击查询按钮")

    def get_query_name(self):
        self.wait(1)
        return self.get_text(loc.query_name,"角色管理-获取查询数据的名称")

    def get_no_data_message(self):
        self.wait(1)
        return self.get_text(loc.no_data, "角色管理-暂无数据")
