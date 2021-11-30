# -*- coding: utf-8 -*-
# @Time : 2021/11/29 16:41
# @Author : Limusen
# @File : system_role_page

from PageLocators.system_locator.system_role_locator import SystemRoleLocator as loc
from Common.base_page import BasePage


class SystemRolePage(BasePage):

    def click_two_button(self):
        self.click(loc.system_tab, "首页-点击系统管理tab")
        self.click(loc.role_tab, "系统管理-点击角色管理tab")

    def create_role(self, **kwargs):
        self.click_two_button()
        self.click(loc.new_role_button, "角色管理-点击新建角色按钮")
        self.wait(1)
        self.input_text(loc.role_name_input, "角色管理-输入角色名称", kwargs['name'])
        self.wait(1)
        self.input_text(loc.role_code_input, "角色管理-输入角色code", kwargs['code'])
        self.wait(1)
        self.click(loc.role_main_button, "角色管理-选择角色权限为首页")
        self.wait(1)
        self.click(loc.accept_button, "角色管理-点击确认按钮")

    def create_role_no_select_group(self, **kwargs):
        self.click_two_button()
        self.click(loc.new_role_button, "角色管理-点击新建角色按钮")
        self.wait(1)
        self.input_text(loc.role_name_input, "角色管理-输入角色名称", kwargs['name'])
        self.wait(1)
        self.input_text(loc.role_code_input, "角色管理-输入角色code", kwargs['code'])
        self.click(loc.accept_button, "角色管理-点击确认按钮")

    def view_user_role(self):
        self.click_two_button()
        self.turn_pages(loc.page_next, "角色管理-翻页按钮")
        self.click(loc.view_group_user_button, "角色管理-查看群组用户按钮")

    def edit_user_role(self):
        self.click_two_button()
        self.turn_pages(loc.page_next, "角色管理-翻页按钮")
        self.get_last_elements(loc.edit_button, "角色管理-点击编辑按钮")
        self.wait(1)
        self.click(loc.click_system_button, "角色管理-点击系统管理按钮")
        self.click(loc.accept_button, "角色管理-点击修改按钮")
        self.wait(1)
        self.get_last_elements(loc.view_group_role_button, "角色管理-查看权限管理")

    def delete_group(self):
        self.click_two_button()
        self.turn_pages(loc.page_next, "角色管理-翻页按钮")
        self.get_last_elements(loc.delete_group_button, "角色管理-删除按钮")
        self.wait(1)
        self.click(loc.delete_accept_button, '角色管理-确认删除按钮')

    def get_role_name(self):
        self.turn_pages(loc.page_next, "角色管理-翻页按钮")
        return self.get_text_elements(loc.get_role_name, "角色管理-获取角色名称")

    def get_error_no_name(self):
        self.wait(1)
        return self.get_text(loc.role_name_null_message, "角色管理-获取未输入角色名称错误提示")

    def get_error_no_code(self):
        self.wait(1)
        return self.get_text(loc.role_code_null_message, "角色管理-获取未输入角色编号错误提示")

    def get_error_no_group(self):
        self.wait(1)
        return self.get_text(loc.role_no_select_message, "角色管理-获取选择群组错误提示")

    def get_no_data_message(self):
        self.wait(1)
        return self.get_text(loc.no_data, "角色管理-暂无数据")

    def get_group_role_name(self):
        return self.get_text_elements(loc.view_group_role, "角色管理-查看群组权限管理")
