# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-01-10 
"""

#python3.6.1
#data：2018-01-03
#author:LGC247CG
"""
说明：
1.该脚本主要是提供一个实现思路，实现方法有很多，可以优化的地方也有很多，触发机制也可以自己设置，代码以压缩到最短，只是为了让大家都可以看明白
2.正常网络状况下，不设置指定时间时，从点击确认验证码到下单基本上1秒左右，所以速度上还是没问题的
3.由于同时勾选多人和单人使用所需时间基本相同，希望该方法只用于技术交流，请勿作为黄牛使用
4.在作为技术交流的情况下，如果验证码可以实现将可以完全实现自动抢票：
--1>验证码有一定规律和数量，可以利用脚本获取所有图片，并加上相应标签
--2>将页面的文字和标签相匹配，再将图片进行相似度计算，对对应图片进行点击操作
--3>或是训练深度学习的图片识别模型，通过算法识别
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.get("https://kyfw.12306.cn/otn/login/init")
browser.find_element_by_id('username').clear()
browser.find_element_by_id('username').send_keys('xxxxxxx')
browser.find_element_by_id('password').send_keys('xxxxxxx')
time.sleep(10)
try:
    browser.find_element_by_id('loginSub').click()
except:
    browser.find_element_by_class_name('touclick-bgimg touclick-reload touclick-reload-normal').click()
    time.sleep(15)
    browser.find_element_by_id('loginSub').click()
#跳转到车票预定页面
time.sleep(2)
clickReserve = browser.find_element_by_link_text('车票预订').click()
#出发地点和到达地点设置
WebDriverWait(browser,10).until(EC.presence_of_element_located((By.ID, "fromStation")))
jsf = 'var a = document.getElementById("fromStation");a.value = "BJP"'
browser.execute_script(jsf)
jst = 'var a = document.getElementById("toStation");a.value = "LZJ"'
browser.execute_script(jst)
js = "document.getElementById('train_date').removeAttribute('readonly')"
browser.execute_script(js)
browser.find_element_by_id('train_date').clear()
browser.find_element_by_id('train_date').send_keys('2018-02-02')
search = browser.find_element_by_id('query_ticket').click()
#对于时间，我一直觉得网站计算的时间和自己获取的时间差一秒左右，这个根据不同环境自己测试
start_time = "Thu Jan 04 10:00:00 2018"
#首先设置需要抢票的时间
b = time.mktime(time.strptime(start_time,"%a %b %d %H:%M:%S %Y"))
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime(b)) )
#此处是为了调试代码使用，可忽略，不影响使用
a = float(b)-time.time()
# #利用自己设置的时间减去当前时间的时间戳
time.sleep(a)
# #上一步骤得出的秒数就是需要等待抢票的时间
browser.find_element_by_id('query_ticket').click()
# #时间到了先点击查询刷新一下，以防找不到元素
try:
    WebDriverWait(browser,10).until(EC.presence_of_element_located((By.ID, "ticket_2400000Z550L")))
    ticket = browser.find_element_by_xpath('//tr[@id="ticket_2400000Z550L"]/td[13]/a').click()
except:
    browser.find_element_by_id('query_ticket').click()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "ticket_250000K8880L")))
    ticket = browser.find_element_by_xpath('//tr[@id="ticket_250000K8880L"]/td[13]/a').click()
"""
normalPassenger_8 数字表示该账号下的第几位，默认从0开始如果是第一个则为normalPassenger_0
"""
WebDriverWait(browser,10).until(EC.presence_of_element_located((By.ID, "normalPassenger_8")))
browser.find_element_by_id('normalPassenger_8').click()
s = Select(browser.find_element_by_id('seatType_1'))
s.select_by_value('6')
browser.find_element_by_id('submitOrder_id').click()
WebDriverWait(browser,10).until(EC.presence_of_element_located((By.ID, "qr_submit_id")))
browser.find_element_by_link_text('提交订单')
#browser.find_element_by_id('qr_submit_id').click()