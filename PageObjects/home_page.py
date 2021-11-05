# -*- coding: utf-8 -*-
# @Time : 2021/11/4 16:20
# @Author : Limusen
# @File : home_page


from Common.base_page import BasePage
from PageLocators.home_locator import HomeLocator as loc


class HomePage(BasePage):

    def is_exit_exist(self):
        """
        如果存在,则返回True,如果不存在,则返回False
        :return:
        """
        try:
            self.wait_ele_visible(loc.exit_loc, "首页-等待[运用后台]元素可见")
        except:
            return False
        else:
            return True
