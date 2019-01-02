# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-03-06 
"""
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests
import sys
import random
import time

sys.path.append(r'D:\CodeWorkspace\python\GeneralTools')
from Ip import Get_Proxies

"""
类说明:下载《笔趣看》网小说《一念永恒》
Parameters:
    无
Returns:
    无
Modify:
    2017-09-13
"""
class downloader(object):

    headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-m2 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.5.506 UWS/2.10.1.22 Mobile Safari/537.36'
    }

    agents = [

        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",

        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",

        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",

        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",

        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",

        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",

        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",

        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",

        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',

        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',

        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',

        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",

        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",

        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",

    ]

    def __init__(self, target_url):
        self.server = 'http://www.biqukan.com/'
        self.target = 'http://www.biqukan.com/' + target_url + '/'
        self.names = []  # 存放章节名
        self.urls = []  # 存放章节链接
        self.nums = 0  # 章节数
        self.session = HTMLSession()

    def process_request(self):
        agent = random.choice(self.agents)
        return agent

    def process_proxy_ip(self):
        ip = Get_Proxies.Get_proxies()
        headers = self.process_request()
        ip_url = 'http://www.xicidaili.com/nn/'
        ip_list = ip.get_ip_list(ip_url, headers=self.headers)
        proxy_ip = ip.get_random_ip(ip_list)
        return proxy_ip

    def download(self, url, num_retries=2):
        # response = requests.get(url)
        headers = self.process_request()
        # proxy_ip = self.process_proxy_ip()
        # proxies = {
        #     'http': proxy_ip,
        #
        # }
        self.session.headers["User-Agent"] = headers
        # self.session.headers["proxies"] = proxies
        response = self.session.get(url)
        if num_retries > 0:
            if 500 <= response.status_code < 600:
                return self.download(url, num_retries - 1)
        return response.text

    """
    函数说明:获取下载链接
    Parameters:
        无
    Returns:
        无
    Modify:
        2017-09-13
    """
    def get_download_url(self, first_chapter):
        # req = requests.get(url = self.target)
        html = self.download(self.target)
        # html = req.text
        div_bf = BeautifulSoup(html, "lxml")
        div = div_bf.find_all('div', class_='listmain')
        a_bf = BeautifulSoup(str(div[0]), "lxml")
        a = a_bf.find_all('a')
        # self.nums = len(a[15:])                                #剔除不必要的章节，并统计章节数
        self.nums = len(a)                                #剔除不必要的章节，并统计章节数
        print(a)
        print(self.nums)

        is_down = 0
        document_num = 0

        for each in a:
            # print('is down %s' % each.get('href'))

            if each.string.find(first_chapter)>=0:
                # print(each.string)
                is_down = 1

            if is_down == 1:
                # print(each.get('href'))
                self.names.append(each.string)
                self.urls.append(self.server + each.get('href'))
                document_num += 1

        self.nums = document_num

    """
    函数说明:获取章节内容
    Parameters:
        target - 下载连接(string)
    Returns:
        texts - 章节内容(string)
    Modify:
        2017-09-13
    """
    def get_contents(self, target):
        # req = requests.get(url = target)
        html = self.download(target)
        # html = req.text
        bf = BeautifulSoup(html, "lxml")
        texts = bf.find_all('div', class_='showtxt')
        # if texts[0] is not None:
        texts = texts[0].text.replace('\xa0'*8, '\n\n')
        return texts

    """
    函数说明:将爬取的文章内容写入文件
    Parameters:
        name - 章节名称(string)
        path - 当前路径下,小说保存名称(string)
        text - 章节内容(string)
    Returns:
        无
    Modify:
        2017-09-13
    """
    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == '__main__':
    #  《一念永恒》'1_1094'  第八十七章
    # 《天道图书馆》 '17_17957'  第一百九十四章
    # 《符界之主》  '39_39432'
    # 系统让我去算命 '54_54833'
    # 美国牧场的小生活 '52_52134'
    # 调频未来 '35_35446'
    # 仙界红包群 16_16643
    # 寒门崛起 0_302
    # 我是天庭扫把星 1_1919
    # 超时空垃圾站 0_124
    # 我在异界有个家 11_11628
    # 三寸人间 52_52561
    # 雷霆之主 54_54918
    # 武道宗师 1_1452
    # 大劫主 0_369
    # 民国谍影 56_56351
    # 大劫主 0_369
    # 核血机心 21_21117
    # 未来游乐场 21_21598
    dl = downloader('21_21598')
    first_chapter = '第1章'
    file_name = '未来游乐场'
    dl.get_download_url(first_chapter)
    time.sleep(random.randint(1, 2))
    print('《%s》开始下载：' % file_name)
    for i in range(dl.nums):
        time.sleep(random.randint(1, 2))
        if dl.urls[i] is not None:
            try:
                text = dl.get_contents(dl.urls[i])
            except:
                try:
                    text = dl.get_contents(dl.urls[i])
                except:
                    continue
            time.sleep(random.randint(1, 2))
            if text is not None:
                dl.writer(dl.names[i], '%s.txt' % file_name, text)
            sys.stdout.write("  已下载:%.3f%%" % float(i/dl.nums) + '\r')
            print('  已下载:{:.3%}'.format(float(i/dl.nums)), '\r')
            print('当前：', i, ' 总计：', dl.nums)
            sys.stdout.flush()
    print('《%s》下载完成' % file_name)