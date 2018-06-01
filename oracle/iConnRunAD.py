#! /usr/bin/env python
# _*_coding:utf-8_*_

import DataEncoding
import parameter
import json
import requests
import six
import time

class run_ad():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }

    def __init__(self, weekId, nextweekid):
        self.week_id = weekId
        self.next_week_id = nextweekid

    def parameter(self, week, type):
        data = {"data": None}
        # 1. run weekId
        para = parameter.parameter(week)
        fridayRun = ""
        if str("All") == type:
            fridayRun = para.AllCountry()
        elif str("JPN") == type:
            fridayRun = para.JPN
        elif str("CHN") == type:
            fridayRun = para.CHN()
        elif str("USA") == type:
            fridayRun = para.USA()
        elif str("Other") == type:
            fridayRun = para.Other()

        encodestr = DataEncoding.DataEncoding(json.dumps(fridayRun))
        encodebody = encodestr.DesEncrypt()

        data["data"] = str(encodebody.replace(b'\n', b'').decode('utf-8'))

        Operation = json.dumps(data)

        return Operation

    def main(self):


        parameter = parameter()

        response = requests.post("http://172.16.1.197:8097/iConn/iconnHandler.do", headers=self.headers, timeout=3, data=parameter)
        print(response.text)

if __name__ == '__main__':
    run = run_ad(201738, 201739)
    run.main()
