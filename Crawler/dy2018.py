#! /usr/bin/env python
# _*_coding:utf-8_*_

import requests
import os
import random
import time
import requests_cache # 为 requests 建立缓存，避免每次执行都去请求一次网页，造成时间浪费

from bs4 import BeautifulSoup

requests_cache.install_cache('demo_cache')

# 伪装浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
}

# 访问的主界面
url = "http://www.dy2018.com/html/gndy/dyzz/index"
for i in range(1,9):
    if (i == 1):
        url = url + ".html"
    else:
        url = url + "_" + str(i) +".html"

    response = requests.get(url, headers=headers)
    html_doc = response.content.decode('gbk') # 由于此网页是 gb2312 编码的，需要转码成 utf8，但 python 貌似不支持 gb2312，所以用 gbk
    # print(html_doc)

    # 提取列表页URL
    soup = BeautifulSoup(html_doc, 'lxml')
    links = []
    for a in soup.select('.ulink'):
        href = 'http://www.dy2018.com' + a['href']
        title = a.string
        links.append(href)
        # print(href, title)

    # 从列表页进入电影页，并提取下载链接
    for link in links:
        response = requests.get(link, headers=headers)
        html_doc = response.content.decode('gbk')
        soup = BeautifulSoup(html_doc, 'lxml')
        ftp_element = soup.select('#Zoom table a')[0] # 由于 select() 的结果是一个数组，所以我们需要选择第一个元素
        download_link = ftp_element['href']
        print(download_link)
        time.sleep(random.randint(1, 2)) # 每次请求一次就让程序睡眠1~2秒，是为了不给对方服务器造成太大压力
