# -*- coding: utf-8 -*-
# @Time : 2021/11/30 14:55
# @Author : Limusen
# @File : system_authority_locator

from selenium.webdriver.common.by import By


class SystemAuthority:
    # 系统管理tab
    system_tab = (By.XPATH, '//div[2]/ul/li[2]/div/div')
    # 权限tab按钮
    authority_tab_button = (By.XPATH, '//div[2]/ul[1]/li[2]/div[1]/ul[1]/li[3]/div[1]')
    # 权限名称输入框
    authority_input = (By.XPATH, '//form[1]/div[1]/div[1]/div[1]/div[1]/input[1]')

    # 查询按钮
    authority_query_button = (By.XPATH, '//form[1]/div[2]/div[1]/button[1]')

    # 翻页按钮
    page_next = (By.XPATH, '//div[2]/div[1]/button[2]')

    # 暂无数据
    no_data = (By.XPATH, '//div[3]/div[1]/span[1]')

    # 获取查询数据
    query_name = (By.XPATH,'//div[3]/table[1]/tbody[1]/tr[1]/td[1]/div[1]')