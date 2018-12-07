# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
-----------------------------------------------------------
 Name：            
 Purpose：         

 Author：          lucas.wang

 Created：         2017-12-23 14:18
 Copyright：       (C) Lucas.wang 2018
 Licence:          MIT
 ----------------------------------------------------------
"""

from parameter import parameter
import DataEncoding
import Path
import json
import requests
import time
import threading
import sys
import pygame
import logging

# 日志模块
logger = logging.getLogger("AppName")
"""
format参数中可能用到的格式化串：
%(name)s             Logger的名字
%(levelno)s          数字形式的日志级别
%(levelname)s     文本形式的日志级别
%(pathname)s     调用日志输出函数的模块的完整路径名，可能没有
%(filename)s        调用日志输出函数的模块的文件名
%(module)s          调用日志输出函数的模块名
%(funcName)s     调用日志输出函数的函数名
%(lineno)d           调用日志输出函数的语句所在的代码行
%(created)f          当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d    输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s                字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d                 线程ID。可能没有
%(threadName)s        线程名。可能没有
%(process)d              进程ID。可能没有
%(message)s            用户输出的消息
"""
formatter = logging.Formatter('%(asctime)s %(levelname)-5s: %(message)s')
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter
logger.addHandler(console_handler)
file_handler = logging.FileHandler("Job.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

class monitor(object):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }

    data = {"data": None}

    job_processed_total_count = {}
    job_stop_count = {}

    url1 = Path.Path()

    def run_ad(self, job_id, url, total_count):
        """
        Get job executing statistic result
        :param job_id:
        :return:
        """
        total_processed_count = 0
        para = parameter(0, job_id)
        friday_run = para.go_on_ad_to_order()

        encode_str = DataEncoding.DataEncoding(json.dumps(friday_run))
        encode_body = encode_str.DesEncrypt()

        self.data["data"] = str(encode_body.replace(b'\n', b'').decode('utf-8'))

        operation = json.dumps(self.data)

        response = requests.post(url, headers=self.headers, timeout=5,
                                 data=operation)

        return_object = json.loads(json.loads(response.text)["string"])

        if int(str(return_object["errorCode"])) == 200:
            if return_object["data"]["totalAdCount"] is not None:
                total_ad_count = list(return_object["data"]["totalAdCount"])
                # print("*******************************************")
                # print(total_ad_count)
                for item in total_ad_count:
                    country_item = dict(item)
                    # print(country_item["countryCode"], country_item["totalProcessedCount"])
                    # logger.info(country_item["countryCode"] + "---" + str(country_item["totalProcessedCount"]))
                    total_processed_count += int(country_item["totalProcessedCount"])

        # print("job id :", job_id, "total count :", total_processed_count)
        logger.info("job id:" + str(job_id) + " --- total count: " + str(total_count) + ", Run total count: " + str(total_processed_count))

        if self.job_processed_total_count is None:
            self.job_processed_total_count[job_id] = total_processed_count
            self.job_stop_count[job_id] = 1
        else:
            hasCount = 0
            print("test count")
            for key, value in self.job_processed_total_count:
                if int(key) == job_id:
                    hasCount = 1
                    if int(value) == total_processed_count:
                        self.job_stop_count[job_id] += 1
                    else:
                        self.job_stop_count[job_id] = 1
            if hasCount == 0:
                self.job_processed_total_count[job_id] = total_processed_count
                self.job_stop_count[job_id] = 1

        for key, value in self.job_stop_count:
            if int(value) > 6:
                logger.info("Job id: " + key + " stop run. please Restart the new thread.".center(80, "】"))


    def is_done(self, job_id, url):
        """
        Check job is done
        :param job_id:
        :return:
        """
        para = parameter(0, job_id)
        friday_run = para.is_finish()

        encode_str = DataEncoding.DataEncoding(json.dumps(friday_run))
        encode_body = encode_str.DesEncrypt()

        self.data["data"] = str(encode_body.replace(b'\n', b'').decode('utf-8'))

        operation = json.dumps(self.data)

        response = requests.post(url, headers=self.headers, timeout=5,
                                 data=operation)

        return_object = json.loads(json.loads(response.text)["string"])

        if int(str(return_object["errorCode"])) == 200:
            # print("job id :", job_id, "done is ", str(return_object["data"]["isDone"]))
            logger.info("job id " + ":" + str(job_id) + "---" + "done is " + str(return_object["data"]["isDone"]))
            return str(return_object["data"]["isDone"])
        else:
            return None

    def is_error(self, job_id, url):
        """
        Check job is done
        :param job_id:
        :return:
        """
        para = parameter(0, job_id)
        friday_run = para.is_error()

        encode_str = DataEncoding.DataEncoding(json.dumps(friday_run))
        encode_body = encode_str.DesEncrypt()

        self.data["data"] = str(encode_body.replace(b'\n', b'').decode('utf-8'))

        operation = json.dumps(self.data)

        response = requests.post(url, headers=self.headers, timeout=10,
                                 data=operation)

        return_object = json.loads(json.loads(response.text)["string"])

        # print(return_object)
        job_str = "job id: " + str(job_id)
        # print(str(job_str).center(50, '='))
        number = 0
        if int(str(return_object["errorCode"])) == 200:
            items = list(return_object["data"]["jobProcessedRecordExecResultList"])
            # print(str(items).center(50, '='))
            for item in items:
                if int(item["errorCode"]) != 200:
                    number += 1
                    logger.info(item)
                    # logger.info(str(item))
            logger.info((str(job_str) + ' error number: ' + str(number)).center(50, '='))

    def main(self):
        job_id = [11346]
        dones = 1
        job_total_count = {}
        job_total_count[11346] = 1027

        t = time.localtime()
        h = t.tm_hour
        m = t.tm_min
        s = t.tm_sec
        w = time.strftime('%w', t)
        # logger.info(h, m, s, w)
        print(h, m, s, w)
        time.sleep(0.3)
        end_date = 23
        str_time = m
        done = None
        dones_id = None
        url = self.url1.dev()

        while True:
            try:
                now = time.localtime()
                if now.tm_hour == end_date:
                    logger.info("End App")
                    sys.exit(0)
                else:
                    if now.tm_min >= str_time:
                        # print("start run:" + str(now.tm_hour) + ":" + str(now.tm_min))
                        logger.info("start run:" + str(now.tm_hour) + ":" + str(now.tm_min))
                        for id in job_id:
                            v = self.filter(job_total_count, id)
                            self.run_ad(id, url, v)
                            time.sleep(10)
                            done = self.is_done(id, url)
                            if int(done) == 1:
                                self.is_error(id, url)
                                dones -= 1
                                dones_id = id
                        logger.info("".center(70, '&'))
                        if dones_id is not None:
                            job_id.remove(dones_id)
                            dones_id = None
                        if int(dones) == 0:
                            break
                        str_time = now.tm_min + 2
                        if str_time >= 60:
                            str_time = 0

                # print("is_done = ", done)
                # if done == "1":
                #     print("&&&&&&&&&&&&&&&&&&")
                #     break
            except Exception as whileEx:
                # print(whileEx)
                logger.info(whileEx)
            finally:
                time.sleep(60)

    def filter(self, data, id):
        # print(data.items())
        # 把字典转换成dict_items，循环里面的key和value，满足if条件返回对应的key和value值
        return {v for k, v in data.items() if k == id}

if __name__ == '__main__':
    monitors = monitor()
    monitors.main()