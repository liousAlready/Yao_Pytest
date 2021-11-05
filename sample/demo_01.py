# -*- coding: utf-8 -*-
# @Time : 2021/11/5 13:51
# @Author : Limusen
# @File : demo_01
import time

from selenium import webdriver

# mac
# driver = webdriver.Chrome("/Users/lishouwu/PycharmProjects/Yao_Pytest/Driver/chromedriver")

# 　win
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
# 等待输入框可见
loc = ("id", "kw")
loc_button = (By.XPATH, '//*[@id="s-top-left"]/a[1]')
driver.implicitly_wait(10)

text = driver.find_element(*loc_button).text
print(text)

driver.find_element(*loc_button).click()



# time.sleep(2)
# base.get_text(loc_button, "获取文本信息")
# time.sleep(2)
# base.input_text(loc, "百度首页_输入搜索内容", "selenium")
# base.click(loc_button, "百度首页_点击搜索按钮")
# time.sleep(2)
# driver.quit()
