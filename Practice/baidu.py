#! /usr/bin/env python
# _*_coding:utf-8_*_
# pip install selenium
# pip install chromedriver

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
kw = driver.find_element_by_id("kw")
kw.clear()
kw.send_keys('白夜追凶')
kw.click()

print(driver.title)

driver.quit()