# -*- coding: utf-8 -*-
# @Time : 2021/11/29 16:28
# @Author : Limusen
# @File : system_role_locator


from selenium.webdriver.common.by import By


class SystemRoleLocator:
    # 系统管理tab
    system_tab = (By.XPATH, '//div[2]/ul/li[2]/div/div')
    # 角色管理tab
    role_tab = (By.XPATH, '//li[2]/div[1]/ul[1]/li[2]/div[1]')

    # 新建角色按钮
    new_role_button = (By.XPATH, '//div[2]/div[2]/button[1]')
    # 角色名称
    role_name_input = (By.XPATH, '//form[1]/div[1]/div[1]/div[1]/input[1]')
    # 　角色识别码
    role_code_input = (By.XPATH, '//form[1]/div[2]/div[1]/div[1]/input[1]')
    # 权限-首页
    role_main_button = (By.XPATH, '//form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]/span[1]')
    # 确定按钮
    accept_button = (By.XPATH, '//div[2]/div[1]/div[1]/button[2]1')

    # 获取角色名称
    get_role_name = (By.XPATH, '//tr[*]/td[1]/div[1]')
    # 未输入用户名报错提示
    role_name_null_message = (By.XPATH, '//form[1]/div[1]/div[1]/div[2]')
    # 未输入code码报错提示
    role_code_null_message = (By.XPATH, '//form[1]/div[2]/div[1]/div[2]')
    # 未选择权限报错提示
    role_no_select_message = (By.XPATH, '/html/body/div[3]/p')

    # 点击查看群组下的用户
    view_group_user_button = (By.XPATH, '//tr[*]/td[2]/div[1]/button[1]/span[1]')

    # 编辑按钮
    edit_button = (By.XPATH, '//td[4]/div[1]/div[1]/span[1]')

    # 选择系统管理
    click_system_button = (By.XPATH,
                           '//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/label[1]/span[1]/span[1]')

    # 查看权限
    view_group_role_button = (By.XPATH, '//td[3]/div[1]/button[1]/span[1]')

    # 查看群组权限
    view_group_role = (By.XPATH, '//div[4]/div[1]/div[2]/div[1]/div[1]/div[*]')

    # 删除群组
    delete_group_button = (By.XPATH, '//td[4]/div[1]/div[1]/span[2]')

    # 确认删除
    delete_accept_button = (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span')

    # 翻页按钮
    page_next = (By.XPATH, '//div[2]/div[1]/button[2]')

    # 暂无数据
    no_data = (By.XPATH, '//div[3]/div[1]/span[1]')
