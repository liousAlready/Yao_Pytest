# encoding: utf-8
# Author    : limusen
# Datetime  : 2021/11/4 10:08 下午
# User      : lishouwu
# Product   : PyCharm
# Project   : Yao_Pytest
# File      : base_page.py
# explain   : 配置文件类

import os
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from Common.log_utils import logger
from Common.config_utils import local_config

current_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_ele_visible(self, locator, page_aciton, timeout=20, poll_frequency=0.5):
        """
        查看元素是否可见
        :param loc:  传入的元素
        :param page_aciton: 所在的页面
        :param timeout: 超时时间
        :param poll_frequency: 等待间隙
        :return:
        """
        logger.info("在 {} 行为，等待元素：{} ".format(page_aciton, locator))
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            # 输入到日志
            logger.exception("当前元素查找不到的原因是：[{}]".format(e.__str__()))
            # 截图
            self.get_page_img(page_aciton)
            raise
        else:
            end = time.time()
            logger.info("等待元素可见成功。等待耗时为: {}".format(end - start))

    def wait_page_contains_element(self, locator, page_aciton, timeout=20, poll_frequency=0.5):
        """
        判断页面是否存在元素
        :param loc:  传入的元素
        :param page_aciton: 所在的页面
        :param timeout: 超时时间
        :param poll_frequency: 等待间隙
        :return:
        """
        logger.info("在 {} 行为，判断页面是否存在元素：{} ".format(page_aciton, locator))
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(locator))
        except Exception as e:
            # 输入到日志
            logger.exception("查找元素失败：[{}]".format(e.__str__()))
            # 截图
            self.get_page_img(page_aciton)
            raise
        else:
            end = time.time()
            logger.info("等待元素可见成功。等待耗时为: {}".format(end - start))

    def get_element(self, locator, page_action, timeout=20, poll_frequency=0.5, wait_exist=False):
        """
        先等待元素可见或存在
        在查找元素
        :param locator: 元素
        :param page_action: 页面操作
        :param wait: 如果为false则走下一步
        :param timeout: 超时时间
        :param poll_frequency: 间隔时间
        :return:
        """
        # 先等待元素可见或者存在
        if wait_exist is False:
            self.wait_page_contains_element(locator, page_action, timeout, poll_frequency)
        else:
            self.wait_ele_visible(locator, page_action, timeout, poll_frequency)

        # 查看元素
        logger.info("在 {} 行为，查看元素：{} ".format(page_action, locator))
        try:
            ele = self.driver.find_element(*locator)
        except Exception as e:
            # 输入到日志
            logger.exception("当前元素查找不到的原因是：[{}]".format(e.__str__()))
            # 截图
            self.get_page_img(page_action)
            raise
        else:
            return ele

    def click(self, locator, page_action, timeout=20, poll_frequency=0.5):
        # 等待 - 查找 -点击
        ele = self.get_element(locator, page_action, timeout, poll_frequency)
        logger.info("在 {} 行为，点击元素：{} ".format(page_action, locator))
        try:
            ele.click()
        except Exception as e:
            # 输入到日志
            logger.exception("点击操作失败！原因是：[{}]".format(e.__str__()))
            # 截图
            self.get_page_img(page_action)
            raise

    def input_text(self, locator, page_action, text, timeout=20, poll_frequency=0.5):
        # 等待 - 查找 - 输入
        ele = self.get_element(locator, page_action, timeout, poll_frequency)
        logger.info("在 {} 行为，给元素：{} , 输入文本: {} ".format(page_action, locator, text))
        try:
            ele.clear()
            ele.send_keys(text)
        except Exception as e:
            # 输入到日志
            logger.exception("点击操作失败！原因是：[{}]".format(e.__str__()))
            # 截图
            self.get_page_img(page_action)
            raise

    def get_text(self):
        pass

    def get_attribute(self):
        pass

    def get_page_img(self, page_action):
        """
        命名规范：{xx页面_xx操作}_截图时间.png
        :return:
        """
        cur_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        file_path = os.path.join(current_path, local_config.get_screen_shot_path)
        file_name = os.path.join(file_path, "{}_{}.png".format(page_action, cur_time))
        self.driver.save_screenshot(file_name)
        logger.info("截图保存在：{}".format(file_name))


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome("/Users/lishouwu/PycharmProjects/Yao_Pytest/Driver/chromedriver")
    base = BasePage(driver)
    driver.get("https://www.baidu.com")
    # 等待输入框可见
    loc = ("id", "kw")
    loc_button = ("id", "su")

    base.input_text(loc, "百度首页_输入搜索内容", "selenium")
    base.click(loc_button, "百度首页_点击搜索按钮")
    time.sleep(2)
    driver.quit()
