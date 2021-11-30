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

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from Common.log_utils import logger
from Common.config_utils import local_config


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def close_browser(self):
        self.driver.close()
        logger.info("关闭当前tab页签")

    def exit_driver(self):
        self.driver.quit()
        logger.info("退出浏览器")

    def back_up(self):
        self.driver.back()
        logger.info("返回上一页")

    def forward(self):
        self.driver.forward()
        logger.info("前进一页")

    def set_window_max(self):
        self.driver.maximize_window()
        logger.info("浏览器最大化")

    def page_refresh(self):
        self.driver.refresh()
        logger.info("浏览器刷新")

    def get_title(self):
        value = self.driver.title
        logger.info("获取标题：%s" % value)
        return value

    def get_url(self):
        value = self.driver.current_url
        logger.info("获取url：%s" % value)
        return value

    def get_page_source(self):
        self.wait(1)
        source = self.driver.page_source
        logger.info("获取页面源码...")
        return source

    def wait(self, seconds=5):
        """
        固定等待--加入默认值，如果没有设置超时时间，则默认等待五秒钟

        :param seconds: 如果没有传入值则默认等待5秒钟
        """
        time.sleep(seconds)
        logger.info("休息一会儿 %s 秒钟~" % seconds)

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

    def get_elements(self, locator, page_action, timeout=20, poll_frequency=0.5, wait_exist=False):
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
            eles = self.driver.find_elements(*locator)
        except Exception as e:
            # 输入到日志
            logger.exception("当前元素查找不到的原因是：[{}]".format(e.__str__()))
            # 截图
            self.get_page_img(page_action)
            raise
        else:
            return eles

    def get_last_elements(self, locator, page_action, timeout=20, poll_frequency=0.5):
        """选择列表最后一个元素"""
        element_list = self.get_elements(locator, page_action, timeout, poll_frequency)
        try:
            element_list[-1].click()
            logger.info("选择列表最后一个元素")
        except Exception as e:
            logger.error("[%s]元素不能识别,原因是: %s" % (locator, e.__str__()))
            self.get_page_img(page_action)

    def get_text_elements(self, locator, page_action, timeout=20, poll_frequency=0.5):
        """选择列表最后一个元素"""
        element_list = self.get_elements(locator, page_action, timeout, poll_frequency)
        try:
            text = element_list[-1].text
            logger.info("选择列表最后一个元素")
            return text
        except Exception as e:
            logger.error("[%s]元素不能识别,原因是: %s" % (locator, e.__str__()))
            self.get_page_img(page_action)

    def turn_pages(self, locator, page_action, timeout=20, poll_frequency=0.5):
        """
        点击翻页按钮到最后一页
        :param locator:
        :param page_action:
        :param timeout:
        :param poll_frequency:
        :return:
        """
        ele = self.get_element(locator, page_action, timeout, poll_frequency)
        logger.info("在 {} 行为，点击元素：{} ".format(page_action, locator))

        while ele.is_enabled():
            if ele.is_enabled():
                ele.click()
            else:
                break

    def click(self, locator, page_action, timeout=20, poll_frequency=0.5):
        """
        对元素进行点击操作
        :param locator:
        :param page_action:
        :param timeout:
        :param poll_frequency:
        :return:
        """
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
        """
        对定位元素进行输入操作
        :param locator:
        :param page_action:
        :param text:
        :param timeout:
        :param poll_frequency:
        :return:
        """
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

    def clear_input(self, locator, page_action, timeout=20, poll_frequency=0.5):
        ele = self.get_element(locator, page_action, timeout, poll_frequency)
        try:
            ele.clear()
        except Exception as e:
            # 输入到日志
            logger.exception("点击操作失败！原因是：[{}]".format(e.__str__()))
            # 截图
            self.get_page_img(page_action)
            raise
        else:
            logger.info("清除内容输入框内容")

    def get_text(self, locator, page_action, timeout=20, poll_frequency=0.5):
        """
        获取文本信息
        :param locator:
        :param page_action:
        :param timeout:
        :param poll_frequency:
        :return:
        """
        ele = self.get_element(locator, page_action, timeout, poll_frequency)
        logger.info("在 {} 行为，获取：{} 元素的文本信息".format(page_action, locator))
        try:
            text = ele.text
        except Exception as e:
            # 输入到日志
            logger.exception("点击操作失败！原因是：[{}]".format(e.__str__()))
            # 截图
            self.get_page_img(page_action)
            raise
        else:
            logger.info("获取到的文本信息是: {}".format(text))
            return text

    def get_attribute(self, locator, page_action, attr, timeout=20, poll_frequency=0.5):
        ele = self.get_element(locator, page_action, timeout, poll_frequency)
        logger.info("在 {} 行为，获取：{} 元素的类型".format(page_action, locator))
        try:
            ele_type = ele.get_attribute(attr)
        except Exception as e:
            # 输入到日志
            logger.exception("点击操作失败！原因是：[{}]".format(e.__str__()))
            # 截图
            self.get_page_img(page_action)
            raise
        else:
            logger.info("获取到的类型是: {}".format(ele_type))
            return ele_type

    def get_page_img(self, page_action):
        """
        命名规范：{xx页面_xx操作}_截图时间.png
        :return:
        """
        cur_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        current_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        file_name = os.path.join(current_path, local_config.get_screen_shot_path,
                                 "{}_{}.png".format(page_action, cur_time))
        self.driver.save_screenshot(file_name)
        logger.info("截图保存在：{}".format(file_name))

    def get_window_handle(self):
        """
        获取所有句柄
        :return:
        """
        return driver.window_handles

    def switch_windows(self, name="new"):
        """
        :param name: 默认跳转到新页面
        :return:
        """
        # 等待 -- 获取句柄 -- 切换句柄
        self.wait(1)
        if name == "new":
            driver.switch_to.window(self.get_window_handle()[-1])

    def switch_to_iframe(self, locator, page_action, timeout=20, poll_frequency=0.5):
        self.wait(1)
        try:
            ele = self.get_element(locator, page_action, timeout, poll_frequency)
            self.driver.switch_to.frame(ele)
        except Exception as e:
            # 输入到日志
            logger.exception("点击操作失败！原因是：[{}]".format(e.__str__()))
            # 截图
            self.get_page_img(page_action)
            raise
        else:
            logger.info("现在跳转框架: {}".format(page_action))

    def switch_to_default(self):
        """
        跳转回原来的框架
        :return:
        """
        try:
            self.wait(1)
            self.driver.switch_to.default_content()
        except Exception as e:
            # 输入到日志
            logger.exception("点击操作失败！原因是：[{}]".format(e.__str__()))
            # 截图
            self.get_page_img("跳转回原框架")
            raise
        else:
            logger.info("调回原来框架")


if __name__ == '__main__':
    from selenium import webdriver

    # mac
    # driver = webdriver.Chrome("/Users/lishouwu/PycharmProjects/Yao_Pytest/Driver/chromedriver")

    # 　win
    driver = webdriver.Chrome()
    base = BasePage(driver)
    driver.get("https://www.baidu.com")

    base.get_page_img("123")
    # 等待输入框可见
    loc = ("id", "kw")
    loc_button = ("id", "su")
    new_button = (By.XPATH, '//*[@id="s-top-left"]/a[1]')
    time.sleep(2)
    base.get_text(new_button, "获取文本信息")

    time.sleep(2)
    base.input_text(loc, "百度首页_输入搜索内容", "selenium")
    base.click(loc_button, "百度首页_点击搜索按钮")
    time.sleep(2)
    driver.quit()
