# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-03-15 
"""
# 引入selenium中的webdriver
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from multiprocessing.dummy import Pool, Lock, freeze_support
import os
import sys
import json

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

def get_json_urls_from_page_url(page_url):
    '''
    获取该专辑页面上所有音频的json链接
    '''
    # webdriver中的PhantomJS方法可以打开一个我们下载的静默浏览器。
    # 输入executable_path为当前文件夹下的phantomjs.exe以启动浏览器
    driver = webdriver.PhantomJS(executable_path="phantomjs.exe")

    # 使用浏览器请求页面
    driver.get(page_url)
    # 加载3秒，等待所有数据加载完毕
    # time.sleep(7)
    driver.implicitly_wait(30)

    # 通过id来定位元素，
    # .text获取元素的文本数据
    # soup = driver.find_element_by_class_name('personal_body')
    mp3_ids = driver.find_element_by_class_name('personal_body').get_attribute('sound_ids')
    # soup = BeautifulSoup(driver.page_source, "lxml")
    #
    # mp3_ids = soup.select_one('.personal_body').attrs['sound_ids']
    # print(mp3_ids)
    # 关闭浏览器
    driver.close()
    json_url = 'http://www.ximalaya.com/tracks/{id}.json'
    urls = [json_url.format(id=i) for i in mp3_ids.split(',')]
    return urls


mp3_json_urls = get_json_urls_from_page_url(page_url)
n_tasks = len(mp3_json_urls)
lock = Lock()
shared_dict = {}




def get_mp3_from_json_url(json_url):
    '''
    访问json链接获取音频名称与下载地址并开始下载
    '''

    driver = webdriver.PhantomJS(executable_path="phantomjs.exe")

    # 使用浏览器请求页面
    driver.get(json_url)
    # 等待所有数据加载完毕
    driver.implicitly_wait(30)

    # 通过id来定位元素，
    # .text获取元素的文本数据
    mp3_info = json.loads(driver.find_element_by_tag_name("pre").text)
    # print(mp3_ids)
    # 关闭浏览器
    driver.close()
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

# if __name__ == '__main__':
#     pass