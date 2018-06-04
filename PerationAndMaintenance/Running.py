#! /usr/bin/env python
# _*_coding:utf-8_*_

import requests
# import requests_cache # 为 requests 建立缓存，避免每次执行都去请求一次网页，造成时间浪费
import time
import threading
import sys
import pygame

'''
pygame.init() 进行全部模块的初始化，
pygame.mixer.init() 或者只初始化音频部分
pygame.mixer.music.load('xx.mp3') 使用文件名作为参数载入音乐 ,音乐可以是ogg、mp3等格式。
    载入的音乐不会全部放到内容中，而是以流的形式播放的，即在播放的时候才会一点点从文件中读取。
pygame.mixer.music.play()播放载入的音乐。该函数立即返回，音乐播放在后台进行。
    play方法还可以使用两个参数
    pygame.mixer.music.play(loops=0, start=0.0) loops和start分别代表重复的次数和开始播放的位置。
pygame.mixer.music.stop() 停止播放，
pygame.mixer.music.pause() 暂停播放。
pygame.mixer.music.unpause() 取消暂停。
pygame.mixer.music.fadeout(time) 用来进行淡出，在time毫秒的时间内音量由初始值渐变为0，最后停止播放。
pygame.mixer.music.set_volume(value) 来设置播放的音量，音量value的范围为0.0到1.0。
pygame.mixer.music.get_busy() 判断是否在播放音乐,返回1为正在播放。
pygame.mixer.music.set_endevent(pygame.USEREVENT + 1) 在音乐播放完成时，用事件的方式通知用户程序，
    设置当音乐播放完成时发送pygame.USEREVENT+1事件给用户程序。 
    pygame.mixer.music.queue(filename) 使用指定下一个要播放的音乐文件，当前的音乐播放完成后自动开始播放指定的下一个。
    一次只能指定一个等待播放的音乐文件。
'''
class ServiceRunning(object):
    """
    Operation and maintenance
    Verify that the server is alive
    """
    pay = pygame.mixer

    def __init__(self):
        # pygame.init()
        self.pay.init()
        self.pay.music.load('./Synchrony - A Broken Delusion.mp3')

    def error(self, error_messages, url):
        """
        Error show function
        :param error_messages:
        :param url:
        :return:
        """
        url80 = ['http://172.16.1.81:8088/iConn/', 'http://172.16.1.82:8097/iConn/',
                 'http://172.16.1.83:8097/iConn/', 'http://172.16.1.84:8097/iConn/']
        set80 = set(url80)
        if url in set80:
            self.pay.music.play()
            print(url)
            print("80 server return error: " + error_messages)
        else:
            print(url)
            print("other server return error: " + error_messages)

    def links(self, url_list):

        """
        # 为 requests 建立缓存，避免每次执行都去请求一次网页，造成时间浪费
        requests_cache.install_cache('demo_cache')

        # 伪装浏览器
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko)
             Chrome/60.0.3112.113 Safari/537.36',
        }
        """

        try:
            for url in url_list:
                try:
                    # response = requests.get(url, headers=headers, timeout=3)
                    status_code = requests.get(url).status_code
                    # print("Server return code:" + str(status_code) + ".(" + url + ")")
                    if status_code != 200:
                        self.error(str(requests.get(url).status_code), url)
                except Exception as ee:
                    print(ee)
                    # print("The server is inaccessible.(" + url + ")")
                    self.error("inaccessible", url)
        except Exception as e:
            print(e)
        finally:
            print("Test connection completed!")

    def get_urls(self):
        """
        Main interface for access
        :return:
        """
        # url_list = ['http://172.16.1.215:8097/iConn/', 'http://172.16.1.197:8097/iConn/',
        #             'http://172.16.1.195:8097/iConn/', 'http://172.16.1.81:8088/iConn/',
        #             'http://172.16.1.82:8097/iConn/', 'http://172.16.1.83:8097/iConn/',
        #             'http://172.16.1.84:8097/iConn/']
        url_list = ['http://172.16.1.197:8097/iConn/', 'http://172.16.1.195:8097/iConn/',
                    'http://172.16.1.81:8088/iConn/', 'http://172.16.1.82:8097/iConn/',
                    'http://172.16.1.83:8097/iConn/', 'http://172.16.1.84:8097/iConn/']

        try:
            t = time.localtime()
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            w = time.strftime('%w', t)
            print(h, m, s, w)
            time.sleep(0.3)
            end_date = 18
            str_time = m

            while True:
                try:
                    now = time.localtime()
                    if now.tm_hour == end_date:
                        self.pay.music.stop()
                        print("End App")
                        sys.exit(0)
                    else:
                        if now.tm_min >= str_time:
                            self.pay.music.stop()
                            print("start run:" + str(now.tm_hour) + ":" + str(now.tm_min))
                            self.links(url_list)
                            str_time = now.tm_min + 2
                            if str_time >= 60:
                                str_time = 0
                except Exception as whileEx:
                    print(whileEx)
                finally:
                    time.sleep(60)

            # while True:
            #     time.sleep(5 * 60)
            #     self.links(url_list)

        except Exception as et:
            print(et)

    def main(self):
        """
        Main function
        :return:
        """
        thread1 = threading.Thread(target=self.get_urls())
        thread1.start()
        thread1.join()
        # self.get_urls()

if __name__ == '__main__':
    run = ServiceRunning()
    run.main()
