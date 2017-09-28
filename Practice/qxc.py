#! /usr/bin/env python
# _*_coding:utf-8_*_

import re
import threading
import time
import os
import requests

def get_qxd_num(html):
    reg = re.compile(r'<td width="40" height="23" align="center" bgcolor=".*?">(.*?)</td>.*?<td align="center" bgcolor=".*?" class="red">(.*?)</td>', re.S)
    list_data = re.findall(reg, html)
    list_str = []
    string = ''

    for i in list_data:
        print(i)
        for j in i:
            print(j)

def get_qxc_html():
    page_num = range(1, 9)
    content = ''

    for page in page_num:
        url = 'http://www.lottery.gov.cn/historykj/history'
        if page_num[page - 1] != 1:
            url += "_" + str(page_num[page - 1])
        url += '.jspx?_ltype=qxc'
        # print(url)

        if requests.get(url).status_code == 404:
            print("error 404")
            continue
        html = requests.get(url, timeout=3)
        get_qxd_num(html.text)


if __name__ == '__main__':
    get_qxc_html()