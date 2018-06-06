# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-01-15 
"""

import json
import requests
import Path
import DataEncoding

class execute(object):
    """
    Execute ad job
    """

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }

    data = {"data": None}

    def __init__(self, version):
        url = Path.Path()
        if str("dev") == version:
            self.url_path = url.dev()
        elif str("release") == version:
            self.url_path = url.release()
        elif str("live") == version:
            self.url_path = url.live()
        else:
            self.url_path = url.dev()
            print("version error!")

        print("Execute", self.url_path)

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

        response = requests.post(self.url_path, headers=self.headers, timeout=3,
                                 data=operation)

        return response

if __name__ == '__main__':
    pass