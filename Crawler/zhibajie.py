# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-02-07 
"""
# coding=utf-8

import requests
import time
from lxml import etree
import sys

sys.path.append(r'D:\CodeWorkspace\python\GeneralTools')
from Ip import Get_Proxies

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
        }
# Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400

def getUrl():
    ip = Get_Proxies.Get_proxies()

    ip_url = 'http://www.xicidaili.com/nn/'
    ip_list = ip.get_ip_list(ip_url, headers=headers)
    ip_len = len(ip_list)
    ip_error_number = 0

    for i in range(33):
        is_success = True

        while is_success:
            is_success = False
            try:
                proxy_ip = ip.get_random_ip(ip_list)
                print(proxy_ip)

                for_spider_page(i, proxy_ip)
            except Exception as e:
                ip_error_number += 1
                is_success = True

        ip_error_number = 0
        # url = 'http://task.zbj.com/t-ppsj/p{}s5.html'.format(i+1)
        #
        # proxy_ip = ip.get_random_ip(ip_list)
        # print(proxy_ip)
        #
        # spiderPage(url, proxy_ip)

def for_spider_page(index, proxy_ip):
    url = 'http://task.zbj.com/t-ppsj/p{}s5.html'.format(index + 1)
    # url = 'http://task.zbj.com/t-rjkf/p{}s5.html'.format(index + 1)
    # url = 'http://task.zbj.com/t-wxptkf/p{}s5.html'.format(index + 1)

    spiderPage(url, proxy_ip)

def spiderPage(url, proxy_ip):
    if url is None:
        return None

    try:
        proxies = {
            'http': proxy_ip,

        }
        htmlText = requests.get(url, headers=headers, proxies=proxies).text

        selector = etree.HTML(htmlText)
        tds = selector.xpath('//*[@class="tab-switch tab-progress"]/table/tr')
        for td in tds:
            price = td.xpath('./td/p/em/text()')
            href = td.xpath('./td/p/a/@href')
            title = td.xpath('./td/p/a/text()')
            subTitle = td.xpath('./td/p/text()')
            deadline = td.xpath('./td/span/text()')
            price = price[0] if len(price)>0 else ''    # python的三目运算 :为真时的结果 if 判定条件 else 为假时的结果
            title = title[0] if len(title)>0 else ''
            href = href[0] if len(href)>0 else ''
            subTitle = subTitle[0] if len(subTitle)>0 else ''
            deadline = deadline[0] if len(deadline)>0 else ''
            print(price,title,href,subTitle,deadline)
            print('---------------------------------------------------------------------------------------')
            spiderDetail(href)
    except Exception as e:
        print('出错', e)


def spiderDetail(url):
    if url is None:
        return None

    try:
        htmlText = requests.get(url).text
        selector = etree.HTML(htmlText)
        aboutHref = selector.xpath('//*[@id="utopia_widget_10"]/div[1]/div/div/div/p[1]/a/@href')
        price = selector.xpath('//*[@id="utopia_widget_10"]/div[1]/div/div/div/p[1]/text()')
        title = selector.xpath('//*[@id="utopia_widget_10"]/div[1]/div/div/h2/text()')
        contentDetail = selector.xpath('//*[@id="utopia_widget_10"]/div[2]/div/div[1]/div[1]/text()')
        publishDate = selector.xpath('//*[@id="utopia_widget_10"]/div[2]/div/div[1]/p/text()')
        aboutHref = aboutHref[0] if len(aboutHref) > 0 else ''  # python的三目运算 :为真时的结果 if 判定条件 else 为假时的结果
        price = price[0] if len(price) > 0 else ''
        title = title[0] if len(title) > 0 else ''
        contentDetail = contentDetail[0] if len(contentDetail) > 0 else ''
        publishDate = publishDate[0] if len(publishDate) > 0 else ''
        print(aboutHref, price, title, contentDetail, publishDate)
    except:
      print('出错')

if __name__ == '__main__':
    getUrl()