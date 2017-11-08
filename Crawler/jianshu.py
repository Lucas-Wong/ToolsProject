#! /usr/bin/env python
# _*_coding:utf-8_*_


import requests
from lxml import etree

class CrawlJs():
    # 爬取数据
    def getArticle(selfs, url):
        print('█████████████◣开始爬取数据')
        my_headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
        }
        request = requests.get(url, headers=my_headers)
        content = request.content

        return content

    # 定义函数，筛选和保存爬取到的数据
    def save(self, content):
        xml = etree.HTML(content)
        title = xml.xpath('//div[@class="content"]/a[@class="title"]/text()')
        link = xml.xpath('//div[@class="content"]/a[@class="title"]/@href')
        print(link)
        i = -1
        for data in title:
            print(data)
            i += 1
            with open('JsIndex.txt', 'a+') as f:
                f.write('[' + str(data.encode('utf-8')) + ']' + '(' + 'http://www.jianshu.com' + str(link[i]) + ')' + '\n')
        print('█████████████◣爬取完成！')

if __name__=='__main__':
    page = int(input('please input page number:'))
    for num in range(page):
        url = 'http://www.jianshu.com/u/c475403112ce?order_by=shared_at&page=%s'%num
        js = CrawlJs()
        content = js.getArticle(url)
        js.save(content)
