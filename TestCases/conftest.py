# -*- coding: utf-8 -*-
# @Time : 2021/11/4 16:02
# @Author : Limusen
# @File : conftest


# 定义fixture - 前置后置 - 作用域 - 返回值

import pytest
from selenium import webdriver
from TestDatas import global_datas as gd


@pytest.fixture(scope="class")
def init():
    # 实例化driver,访问登录页面
    # driver = webdriver.Chrome("/Driver/chromedriver")     # mac地址
    driver = webdriver.Chrome()

    driver.get(gd.base_url)
    yield driver
    driver.quit()


# 调用init方法，先打开浏览器操作，操作完毕之后，刷新页面再重新请求
@pytest.fixture
def refresh(init):
    init.refresh()
    yield init
