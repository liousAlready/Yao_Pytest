# -*- coding: utf-8 -*-
# @Time : 2021/11/11 14:55
# @Author : Limusen
# @File : system_page

from PageLocators.system_locator import SystemLocator as loc
from Common.base_page import BasePage


class SystemPage(BasePage):

    def query_name(self, name):
        self.click(loc.system_tab, "首页-点击系统管理tab")
        self.click(loc.insider_click, "系统管理-点击内部人员管理tab")
        self.input_text(loc.username_input, "内部人员管理-输入姓名", name)
        self.click(loc.select_click, "内容人员管理-点击查询按钮")

    def get_query_name_text(self):
        return self.get_text(loc.second_value, "内容人员管理-获取姓名")

    def query_null(self):
        return self.get_text(loc.null_data, "查询结果为暂无数据")
