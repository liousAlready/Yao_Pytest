# -*- coding: utf-8 -*-
# @Time : 2021/11/4 16:02
# @Author : Limusen
# @File : conftest


# 定义fixture - 前置后置 - 作用域 - 返回值

import pytest
from selenium import webdriver
from TestDatas import global_datas as gd


@pytest.fixture
def init():
    # 实例化driver,访问登录页面
    driver = webdriver.Chrome()
    driver.get(gd.base_url)
    yield driver
    driver.quit()