#! /usr/bin/env python
# _*_coding:utf-8_*_
import requests
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool, Lock, freeze_support
import os
import sys
from requests_html import HTMLSession
import random


# http://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
def input_page_url_with_change_dir():
    '''
    转移到要存储的文件夹位置并获取专辑页面地址
    '''
    print('请输入存储文件夹(回车确认):')
    while True:
        dir_ = input()
        if os.path.exists(dir_):
            os.chdir(dir_)
            break
        else:
            try:
                os.mkdir(dir_)
                os.chdir(dir_)
                break
            except Exception as e:
                print('请输入有效的文件夹地址:')

    print('请输入想下载FM页面的网址(回车确认) -\n'
          '如 http://www.ximalaya.com/20251158/album/2758791：')
    page_url = input()
    return page_url


page_url = input_page_url_with_change_dir()

# headers = {
#     'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                    'Chrome/57.0.2987.133')
# }
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


def process_request():
    agent = random.choice(agents)
    return agent

def download(url, num_retries=2):
    session = HTMLSession()
    headers = process_request()
    session.headers["User-Agent"] = headers
    response = session.get(url)
    if num_retries > 0:
        if 500 <= response.status_code < 600:
            return download(url, num_retries - 1)
    return response.text

def get_json_urls_from_page_url(page_url):
    '''
    获取该专辑页面上所有音频的json链接
    '''
    # res = requests.get(page_url, headers=headers)
    # # soup = BeautifulSoup(res.content, "html5lib")
    # soup = BeautifulSoup(res.content, "lxml")
    soup = download(page_url)
    print(soup)
    mp3_ids = soup.select_one('.personal_body').attrs['sound_ids']
    json_url = 'http://www.ximalaya.com/tracks/{id}.json'
    urls = [json_url.format(id=i) for i in mp3_ids.split(',')]
    return urls


mp3_json_urls = get_json_urls_from_page_url(page_url)
n_tasks = len(mp3_json_urls)
lock = Lock()
shared_dict = {}
# 对字典的单步写操作为原子操作，不用考虑竞态，见下参考
# https://docs.python.org/3.6/faq/library.html#what-kinds-of-global-value-mutation-are-thread-safe
# http://stackoverflow.com/questions/6953351/thread-safety-in-pythons-dictionary
# d = {1:1}; import dis; dis.dis('d[1] = "x"')
# http://document.ihg.uni-duisburg.de/Documentation/Python/lib/node56.html


def get_mp3_from_json_url(json_url):
    '''
    访问json链接获取音频名称与下载地址并开始下载
    '''
    session = HTMLSession()
    headers = process_request()
    session.headers["User-Agent"] = headers
    mp3_info = session.get(json_url)
    # mp3_info = requests.get(json_url, headers=headers).json()
    title = mp3_info['album_title'] + '+ ' + mp3_info['title'] + '.m4a'
    path = mp3_info['play_path']
    title = title.replace('|', '-')  # 避免特殊字符文件名异常

    if os.path.exists(title):
        return 'Already exists!'

    # http://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
    while True:
        try:
            with open(title, 'wb') as f:
                response = requests.get(path, headers=headers, stream=True)

                if not response.ok:
                    # shared_dict.pop(title)
                    print('response error with', title)
                    continue

                total_length = int(response.headers.get('content-length'))

                chunk_size = 4096
                dl = 0
                shared_dict[title] = 0

                for block in response.iter_content(chunk_size):
                    dl += len(block)
                    f.write(block)
                    done = int(50 * dl / total_length)
                    shared_dict[title] = done

                global n_tasks
                with lock:
                    n_tasks -= 1
                shared_dict.pop(title)
                return 'Done!'

        except Exception as e:
            print('other error with', title)
            os.remove(title)


# http://stackoverflow.com/questions/28057445/python-threading-multiline-progress-report
# http://stackoverflow.com/questions/15644964/python-progress-bar-and-downloads
def report_status():
    '''
    根据共享字典汇报下载进度
    '''
    import time
    n = len(mp3_json_urls)

    print(u'准备下载...')
    while len(shared_dict) == 0:
        time.sleep(0.2)

    while len(shared_dict) != 0:
        line = ''  # "\r"
        for title, done in shared_dict.items():
            line += "%s\n - [%s%s]\n" % (
                title, '=' * done, ' ' * (50 - done)
            )
        line += '\n**** 剩余/总任务 = %s/%s ****' % (n_tasks, n)
        os.system('cls')
        sys.stdout.write(line)
        sys.stdout.flush()
        time.sleep(1)


# if __name__ == '__main__':
# 多线程下载并报告状态
freeze_support()
with Pool(6) as pool:
    # http://stackoverflow.com/questions/35908987/python-multiprocessing-map-vs-map-async
    r = pool.map_async(get_mp3_from_json_url, mp3_json_urls)
    report_status()
    r.wait()
    os.system('cls')
    print('下载完成！')


# http://stackoverflow.com/questions/28349359/pyinstaller-single-file-executable-doesnt-run
# pyinstaller ximalaya3.py --onefile --noupx
# https://greasyfork.org/zh-CN/scripts/24662-%E5%96%9C%E9%A9%AC%E6%8B%89%E9%9B%85%E9%9F%B3%E4%B9%90%E4%B8%8B%E8%BD%BD/code
