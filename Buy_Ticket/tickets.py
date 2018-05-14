#! /usr/bin/env python
#_*_coding:utf-8_*_

"""Train tickets query via command-line.
Usage:
    tickets [-gdtkz] <from> <to> <date>
Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达
Example:
    tickets beijing shanghai 2016-08-25
"""
from docopt import docopt
from TrainCollectio import TrainCollection
import requests
import re
import certifi
import urllib3

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
}

def cli():
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955'
    r = requests.get(url)
    # r = http.request('GET', url)
    stations = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', r.text)
    station = dict(stations)

    arg = docopt(__doc__)
    from_station = station.get(arg['<from>'])
    to_station = station.get(arg['<to>'])
    date = arg['<date>']

    print(to_station)
    url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={}'.format(
        date, from_station, to_station
    )
    r = requests.get(url)
    # r = http.request('GET', url)
    rows = r.json()['data']['datas']
    trains = TrainCollection(rows)
    trains.pretty_print()

if __name__ == '__main__':
    cli()