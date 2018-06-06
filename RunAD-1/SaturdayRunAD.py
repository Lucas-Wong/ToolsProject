#! /usr/bin/env python
# _ * _ coding:utf-8 _ * _

import json
import requests
import parameter
import DataEncoding
import Path

class SaturdayRunAD(object):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }

    data = {"data": None}

    def __init__(self, current_week, version):
        self.week = current_week
        if str("dev") == version:
            self.url = Path.dev()
        elif str("release") == version:
            self.url = Path.release()
        elif str("live") == version:
            self.url = Path.live()

    def main(self):
        pass

if __name__ == '__main__':
    SaturdayRunAD(201750, 'dev')