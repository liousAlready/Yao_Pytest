# -*- coding: utf-8 -*-
# @Time : 2021/11/4 18:23
# @Author : Limusen
# @File : login_datas


# 登录成功的测试数据
valid_user = ("13252254992","254992")

# 登录失败的数据
invalid_data = [
    {"user": "", "passwd": "254992", "check": "请输入手机号"},
    {"user": "13252254992", "passwd": "", "check": "请输入密码"},
    {"user": "", "passwd": "", "check": "请输入手机号"}
]
