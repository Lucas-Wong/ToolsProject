# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-03-16 
"""

from selenium import webdriver
import time
from multiprocessing.dummy import Pool, Lock, freeze_support
import os
import sys
import json

# webdriver中的PhantomJS方法可以打开一个我们下载的静默浏览器。
# 输入executable_path为当前文件夹下的phantomjs.exe以启动浏览器
driver = webdriver.PhantomJS(executable_path="phantomjs.exe")

# 使用浏览器请求页面
# driver.get("http://www.ximalaya.com/25504353/album/3229729/")
# driver.get("http://www.ximalaya.com/tracks/28747505.json")
driver.get('http://audio.xmcdn.com/group23/M09/89/CA/wKgJL1h5wBHw1AU3AI1VDZ6xCwg496.m4a')
# 加载3秒，等待所有数据加载完毕
# time.sleep(7)
driver.implicitly_wait(30)

# 通过id来定位元素，
# .text获取元素的文本数据
# soup = driver.find_element_by_class_name('personal_body')
# mp3_ids = driver.find_element_by_class_name('personal_body').get_attribute('sound_ids')
# soup = BeautifulSoup(driver.page_source, "lxml")
#
# mp3_ids = soup.select_one('.personal_body').attrs['sound_ids']
# print(mp3_ids)

# mp3_info = json.loads(driver.find_element_by_tag_name("pre").text)
# print(mp3_info)

print(driver.page_source)
# 关闭浏览器
driver.close()

# json_url = 'http://www.ximalaya.com/tracks/{id}.json'
# urls = [json_url.format(id=i) for i in mp3_ids.split(',')]
# for url in urls:
#     print(url)
# if __name__ == '__main__':
#     pass