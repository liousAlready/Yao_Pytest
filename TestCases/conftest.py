# -*- coding: utf-8 -*-
# @Time : 2021/11/4 16:02
# @Author : Limusen
# @File : conftest


# 定义fixture - 前置后置 - 作用域 - 返回值
import os
import pytest
import allure
from TestDatas import global_datas as gd
from PageObjects.login_ob.login_page import LoginPage
from Common.browser import Browser
from Common.config_utils import local_config

driver = None
current_path = os.path.dirname(os.path.dirname(__file__))
failures_path = os.path.join(current_path, local_config.error_file_path, 'failures')


@pytest.fixture(scope='session', autouse=True)
def browser():
    """
    定义一个总的调用driver的方法，用例中直接调用browser
    :return:
    """
    global driver
    if driver is None:
        driver = Browser().get_driver()
        driver.maximize_window()
        driver.get(gd.base_url)
        LoginPage(driver).login(*gd.admin_user)
    yield driver
    driver.quit()


# 调用init方法，先打开浏览器操作，操作完毕之后，刷新页面再重新请求
@pytest.fixture
def refresh(browser):
    yield browser
    browser.refresh()


# 用例失败后自动截图 钩子函数
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    获取用例执行结果的钩子函数
    :param item:
    :param call:
    :return:
    """
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        mode = "a" if os.path.exists(failures_path) else "w"
        with open(failures_path, mode)as f:
            if "tmpir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
                f.write(report.nodeid + extra + "\n")
            with allure.step('添加失败截图...'):
                allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
