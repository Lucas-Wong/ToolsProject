# -*- coding: utf-8 -*-
"""
-----------------------------------------------------
    File Name:        execute
    Author:           Lucas.wang
    Date:             2019-02-06 17:05
    Description:      
-----------------------------------------------------
    Change Activity:  2019-02-06 17:05
    Description:      
----------------------------------------------------
"""
import json
import requests
import url_path
import data_encoding

class execute(object):
    """
    Execute ad job
    """

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }

    data = {"data": None}


    def __init__(self, company, version):
        path = url_path()
        path.rtn_url(company, version)

    def post(self, run_json):
        """
        Post
        :param run_json:
        :return:
        """

        print("Execute", run_json)

        encode_str = data_encoding.DataEncoding(json.dumps(run_json))
        encode_body = encode_str.DesEncrypt()

        self.data["data"] = str(encode_body.replace(b'\n', b'').decode('utf-8'))

        operation = json.dumps(self.data)

        # print(operation)

        response = requests.post(self.url_path, headers=self.headers, timeout=3,
                                 data=operation)

        return response

if __name__ == '__main__':
    pass
