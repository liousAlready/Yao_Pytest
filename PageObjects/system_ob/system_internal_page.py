# -*- coding: utf-8 -*-
# @Time : 2021/11/11 14:55
# @Author : Limusen
# @File : system_page

from PageLocators.system_locator.system_internal_locator import SystemInternal as loc
from Common.base_page import BasePage


class SystemPage(BasePage):

    def click_two_button(self):
        self.click(loc.system_tab, "首页-点击系统管理tab")
        self.click(loc.insider_click, "系统管理-点击内部人员管理tab")

    def name_query(self, name):
        self.input_text(loc.username_input, "内部人员管理-输入姓名", name)
        self.click(loc.select_click, "内容人员管理-点击查询按钮")
        self.wait(1)
        return self.get_text(loc.second_value, "内容人员管理-获取姓名")

    def query_name(self, name):
        self.click_two_button()
        self.input_text(loc.username_input, "内部人员管理-输入姓名", name)
        self.click(loc.select_click, "内容人员管理-点击查询按钮")

    def query_status_online(self):
        self.click_two_button()
        self.click(loc.click_status, "内容人员管理-点击状态栏")
        self.click(loc.incumbency_status, "状态栏-点击在职按钮")
        self.click(loc.select_click, "内容人员管理-点击查询按钮")

    def query_status_quit(self):
        self.click_two_button()
        self.click(loc.click_status, "内容人员管理-点击状态栏")
        self.click(loc.quit_status, "状态栏-点击离职按钮")
        self.click(loc.select_click, "内容人员管理-点击查询按钮")

    def query_phone(self, phone):
        self.click_two_button()
        self.input_text(loc.input_phone, "内容人员管理-电话号码输入框", phone)
        self.click(loc.select_click, "内容人员管理-点击查询按钮")

    def create_user(self, **kwargs):
        self.click_two_button()
        self.click(loc.add_user_button_click, "内容人员管理-新增用户")
        self.input_text(loc.add_user_name, "内容人员管理-填写用户名", kwargs['name'])
        self.input_text(loc.add_user_phone, "内容人员管理-填写手机号", kwargs['phone'])
        self.wait(1)
        self.click(loc.role_click, "内容人员管理-点击选择群组下拉框")
        self.wait(1)
        self.click(loc.add_user_role, "内容人员管理-选择群组")
        self.wait(1)
        self.click(loc.add_button, "内容人员管理-点击确认按钮")
        self.click(loc.select_click, "内容人员管理-点击查询按钮")

    def create_user_no_query(self, **kwargs):
        self.click_two_button()
        self.click(loc.add_user_button_click, "内容人员管理-新增用户")
        self.input_text(loc.add_user_name, "内容人员管理-填写用户名", kwargs['name'])
        self.input_text(loc.add_user_phone, "内容人员管理-填写手机号", kwargs['phone'])
        self.wait(1)
        self.click(loc.role_click, "内容人员管理-点击选择群组下拉框")
        self.wait(1)
        self.click(loc.add_user_role, "内容人员管理-选择群组")
        self.wait(1)
        self.click(loc.add_button, "内容人员管理-点击确认按钮")

    def create_user_fail_name(self, **kwargs):
        self.click_two_button()
        self.click(loc.add_user_button_click, "内容人员管理-新增用户")
        self.wait(1)
        self.input_text(loc.add_user_name, "内容人员管理-填写用户名", kwargs['name'])
        self.input_text(loc.add_user_phone, "内容人员管理-填写手机号", kwargs['phone'])
        self.click(loc.add_button, "内容人员管理-点击确认按钮")
        self.wait(2)

    def create_user_all_null(self):
        self.click_two_button()
        self.click(loc.add_user_button_click, "内容人员管理-新增用户")
        self.click(loc.add_button, "内容人员管理-点击确认按钮")
        self.wait(2)

    def set_user_quit(self, ):
        self.click_two_button()
        self.wait(1)
        self.turn_pages(loc.page_next,"内容人员管理-翻页按钮")
        self.wait(1)
        self.get_last_elements(loc.quit_text,"内容人员管理-离职按钮")
        self.click(loc.accpet,"内容人员管理-离职二次确认按钮")

    def edit_user_group(self):
        self.click_two_button()
        self.wait(1)
        self.turn_pages(loc.page_next,"内容人员管理-翻页按钮")
        self.wait(1)
        self.get_last_elements(loc.edit_button, "内容人员管理-编辑按钮")
        self.wait(1)
        self.click(loc.role_click,"内容人员管理-选择群组按钮")
        self.wait(1)
        self.get_last_elements(loc.group,"内容人员管理-选择ui群组按钮")
        self.click(loc.add_button,"内容人员管理-点击修改按钮")

    def get_quit_message(self):
        self.wait(1)
        return self.get_text_elements(loc.quit_message,"内容人员管理-查看是否离职")

    def get_edit_group_message(self):
        self.wait(1)
        return self.get_text_elements(loc.group_message, "内容人员管理-查看是否修改群组")

    def get_fail_name_text(self):
        self.wait(1)
        return self.get_text(loc.fail_name_message, "内容人员管理-不输入姓名获取失败文案")

    def get_fail_phone_text(self):
        self.wait(1)
        return self.get_text(loc.fail_phone_message, "内容人员管理-不输入手机号获取失败文案")

    def get_fail_role_text(self):
        self.wait(1)
        return self.get_text(loc.fail_role_message, "内容人员管理-不输入姓名获取失败文案")

    def get_query_name_text(self):
        self.wait(1)
        return self.get_text(loc.second_value, "内容人员管理-获取姓名")

    def query_null(self):
        self.wait(1)
        return self.get_text(loc.null_data, "查询结果为暂无数据")

    def is_fail_name_message(self):
        """
        如果存在,则返回True,如果不存在,则返回False
        :return:
        """
        try:
            self.wait_ele_visible(loc.fail_name_message, "内容人员管理-不输入姓名获取失败文案可见")
        except:
            return False
        else:
            return True
