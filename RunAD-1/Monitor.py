#! /usr/bin/env python
#_*_coding:utf-8_*_

import json
import requests
import Path

class Monitor(object):
    """
    Monitor run AD
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }

    data = {"data": None}
    processed_count = {}

    def __init__(self, current_week, job_id, version, job_total_count):
        self.week = current_week
        if str("dev") == version:
            self.url = Path.dev()
        elif str("release") == version:
            self.url = Path.release()
        elif str("live") == version:
            self.url = Path.live()

        self.job_id = []
        self.job_id = job_id
        self.job_total_count = job_total_count

    def friday_run_ad(self):
        """
        Get Job Executing Statistic Result
        :return:
        """
        para = parameter.parameter(0, self.job_id)
        friday_run = para.go_on_ad_to_order()
        total_count = 0

        encode_str = DataEncoding.DataEncoding(json.dumps(friday_run))
        encode_body = encode_str.DesEncrypt()

        self.data["data"] = str(encode_body.replace(b'\n', b'').decode('utf-8'))

        operation = json.dumps(self.data)

        response = requests.post(self.url, headers=self.headers, timeout=3,
                                 data=operation)
        print(response.text)

        processed = json.loads(json.loads(response.text)["string"])

        if int(str(processed["errorCode"])) == 200:
            total_ad_count = processed["data"]["totalAdCount"]
            for country_total_count in total_ad_count:
                print(country_total_count)
                total_count += int(json.loads(country_total_count)["totalProcessedCount"])

        return total_count

    def friday_payment(self):
        pass

    def saturday_run_ad(self):
        pass

    def is_done(self):
        """
        Check Job Is Done Hanlder
        :return:
        """
        para = parameter.parameter(0, self.job_id)
        friday_run = para.is_finish()
        is_done = 0

        encode_str = DataEncoding.DataEncoding(json.dumps(friday_run))
        encode_body = encode_str.DesEncrypt()

        self.data["data"] = str(encode_body.replace(b'\n', b'').decode('utf-8'))

        operation = json.dumps(self.data)

        response = requests.post(self.url, headers=self.headers, timeout=3,
                                 data=operation)

        return_object = json.loads(json.loads(response.text)["string"])

        if int(str(return_object["errorCode"])) == 200:
            print(str(self.job_id) + ": " + str(return_object["data"]["isDone"]))
            is_done = int(return_object["data"]["isDone"])

        return is_done


    def main(self):
        pass

if __name__ == '__main__':
    Monitor()