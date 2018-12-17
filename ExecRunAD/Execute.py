# _*_ coding:utf-8 _*_
"""
-----------------------------------------------------------
 Name：            ToolsProject/Execute
 Purpose：         Execute API Data

 Author：          lucas.wang

 Created：         2018-07-30
 Copyright：       (C) lucas.wang 2018
 Licence:          MIT
 ----------------------------------------------------------
"""
# ! /usr/bin/env python

import json
import requests
import DataEncoding
import logging
import logging.config
import os

filepath = os.path.join(os.path.dirname(__file__), 'logging.conf')
logging.config.fileConfig(filepath)
logger_name = "AppName"
logger = logging.getLogger(logger_name)

class execute(object):
    """
    Execute ad job
    """

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }

    data = {"data": None}

    def __init__(self, url):
        self.url_path = url

    def post(self, run_json):
        """
        Post
        :param run_json:
        :return:
        """

        print("Execute", run_json)

        encode_str = DataEncoding.DataEncoding(json.dumps(run_json))
        encode_body = encode_str.DesEncrypt()

        self.data["data"] = str(encode_body.replace(b'\n', b'').decode('utf-8'))

        operation = json.dumps(self.data)

        # print(operation)
        # print(self.url_path)
        # print(self.headers)

        response = requests.post(self.url_path, headers=self.headers, timeout=3,
                                 data=operation)


        return response

if __name__ == '__main__':
    pass