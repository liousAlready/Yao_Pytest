# -*- coding: utf-8 -*-
# @Time : 2021/11/11 14:50
# @Author : Limusen
# @File : system_locator


from selenium.webdriver.common.by import By


class SystemLocator:
    # 系统管理tab
    system_tab = (By.XPATH, '//div[2]/ul/li[2]/div/div')
    # 内部人员管理
    insider_click = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/div/div[2]/ul/li[2]/div/ul/li[1]/div')
    # 姓名输入框
    username_input = (By.XPATH, '//input[@placeholder="请输入成员姓名" ]')
    # 查询按钮
    select_click = (
        By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[2]/form/div[4]/div/button[1]')

    # 获取列表第二个值
    second_value = (By.XPATH, '//*/tr/td[2]')

    # 暂无数据
    null_data = (By.XPATH, '//*/div[3]/div/span')

    # #    查询成功的内部用户
    # select_name_pass = (By.XPATH,'//*[@class="el-table_1_column_2  "]')
    # 点击状态
    click_status = (By.XPATH, '//*/div[2]/div[1]/div[1]/div[1]/input')
    #     查询状态 - 在职
    incumbency_status = (By.XPATH, '//body/div[2]/div[1]/div[1]/ul/li[1]')
    #     查询状态 - 离职
    quit_status = (By.XPATH, '//body/div[2]/div[1]/div[1]/ul/li[2]')
    # #     离职人员
    # quit_userid = (By.XPATH,'//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[4]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div')

    #     输入手机号
    input_phone = (By.XPATH, '//*[@placeholder="请输入手机号"]')

    #     新增用户按钮
    add_user_button_click = (By.XPATH, '//div[2]/div[3]/button')
    #     新增用户名
    add_user_name = (By.XPATH, '//form/div[1]/div[1]/div[1]/input')
    #     新增手机号
    add_user_phone = (By.XPATH, '//form/div[2]/div[1]/div[1]/input')
    #     新增角色 - -选择群组
    add_user_role = (By.XPATH, '//div[1]/div[1]/ul/li[4]')
    #     新增角色
    role_click = (By.XPATH, '//div[1]/form/div[3]/div[1]/div[1]/div[1]/input')
    #     新增用户 - 确认按钮
    add_button = (
    By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div/div[3]/div/div[2]/div/form/div[4]/div/button[2]')
    #     点击离职按钮
    quit_user_button = (By.XPATH,
                        '//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[4]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div/button[2]/span')
    #     离职二次确认按钮
    quit_second_button = (By.XPATH,
                          '//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[4]/div[1]/div[3]/table/tbody/tr/td[7]/div/button[1]/span')
    #     编辑用户群组
    edit_user = (By.XPATH, '//*/div[1]/div[1]/ul/li[6]')
    #     点击用户群组
    edit_role_click = (By.XPATH,
                       '//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div/div[3]/div/div[2]/div/form/div[4]/div/button[2]/span')
    #     选择新群组
    edit_role_list_select = (By.XPATH,
                             '//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[4]/div[1]/div[3]/table/tbody/tr/td[5]/div/span')
    #     修改按钮
    edit_confirm = (By.XPATH,
                    '//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[4]/div[1]/div[3]/table/tbody/tr/td[4]/div')

    fail_name_message = (By.XPATH, '//form/div[1]/div/div[2]')

    fail_phone_message = (By.XPATH,'//form[1]/div[2]/div[1]/div[2]')

    fail_role_message= (By.XPATH,'//form[1]/div[3]/div[1]/div[2]')

    # #     离职
    # quit_text = (By.XPATH,)
    # #     当前所在群组
    # now_group = (By.XPATH,)
    # #     重复的手机号码
    # repeat_phone_tips = (By.XPATH,)
    # #     手机号码格式错误
    # phone_format_error = (By.XPATH,)
    # #     暂无数据
    # no_data = (By.XPATH,)
