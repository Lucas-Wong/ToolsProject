# ! /usr/bin/env python
# _*_ coding:utf-8 _*_

import json
import requests
import parameter
import DataEncoding
import Path

class FridayRunAD(object):
    """
    Friday run ad use
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }

    data = {"data": None}

    def __init__(self, current_week, version):
        self.week = current_week
        url1 = Path.Path()
        if str("dev") == version:
            self.url = url1.dev()
        elif str("release") == version:
            self.url = url1.release()
        elif str("live") == version:
            self.url = url1.live()
        else:
            print("version error")

    def run_ad(self) -> json:
        """
        Run ad use
        :return: service return json
        """

        print(self.url)

        para = parameter.parameter(self.week, 0)
        friday_run = para.AllCountry()

        print(friday_run)

        encode_str = DataEncoding.DataEncoding(json.dumps(friday_run))
        encode_body = encode_str.DesEncrypt()

        self.data["data"] = str(encode_body.replace(b'\n', b'').decode('utf-8'))

        operation = json.dumps(self.data)

        # print(operation)

        response = requests.post(self.url, headers=self.headers, timeout=3,
                                 data=operation)
        # print(response.text)

        return json.loads(response.text)["string"]

    def payment_ad(self):
        pass

    def main(self):
        """
        main function
        test use
        """
        self.run_ad()
        self.payment_ad()


if __name__ == '__main__':
    friday = FridayRunAD(201750, 'dev')
    friday.main()
