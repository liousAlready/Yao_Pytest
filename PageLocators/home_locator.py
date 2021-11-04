# -*- coding: utf-8 -*-
# @Time : 2021/11/4 19:25
# @Author : Limusen
# @File : home_locator


from selenium.webdriver.common.by import By


class HomeLocator:
    # 运营后台标题
    exit_loc = (By.XPATH, '//div[@class="logo open"]/span')
