#! /usr/bin/env python
#  _*_coding:utf-8_*_
"""
document note
"""
import re
import threading
import time
import os
import requests

PYTHONIOENCODING = 'utf-8'

class Archives(object):
    def save_links(self, url):
        """
        this is save file
        """
        links = []
        links_dict = {}
        name = []
        count = 0
        try:
            print(url)
            data = requests.get(url, timeout=3)
            content = data.text
            link_pat = '"(ed2k://\|file\|[^"]+?\.(S\d+)(E\d+)[^"]+?1024X\d{3}[^"]+?)"'
            name_pat = re.compile(r'<h2 class="entry_title">(.*?)</h2>', re.S)
            links = set(re.findall(link_pat, content))
            print(links)
            name = re.findall(name_pat, content)
            count = len(links)
        except Exception as ee:
            print("2", ee)
            pass
        for i in links:
            # 把剧集按s和e提取编号
            links_dict[int(i[1][1:3]) * 100 + int(i[2][1:3])] = i
            print(i)
        try:
            print(name)
            print(os.getcwd() + name[0].replace('/', ' '))
            with open(file='D:\\CodeWorkspace\\videos\\' + name[0].replace('/', ' ') + '.txt', mode='a', encoding='utf-8') as f:
                # with open('D:\\CodeWorkspace\\test.txt','a','utf8') as f:
                # 按季数+集数排序顺序写入
                for i in sorted(list(links_dict.keys())):
                    f.write(links_dict[i][0] + '\n')
            print("8 Get links ... ", name[0], count)
        except Exception as ex:
            print("3", ex)
            pass

    def get_urls(self):
        try:
            for i in range(2015, 25000):
                base_url = 'http://cn163.net/archives/'
                url = base_url + str(i) + '/'
                if requests.get(url).status_code == 404:
                    print("error 404")
                    continue
                else:
                    self.save_links(url)
        except Exception as et:
            print("1", et)
            pass

    def main(self):
        thread1 = threading.Thread(target=self.get_urls())
        thread1.start()
        thread1.join()

if __name__ == '__main__':
    startTime = time.time()
    a = Archives()
    a.main()
    endTime = time.time()
    print(endTime-startTime)
