# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-02-07 
"""

import requests
from bs4 import BeautifulSoup

url = "http://www.pm25x.com/"
html = requests.get(url)
spl = BeautifulSoup(html.text, "html.parser")
# print(spl)

city = spl.find("a", {"title": "天津PM2.5"})
# print(city)
# city = spl.select(".天津PM2.5") # error, no have data
# print(city)

citylink = city.get("href")

url2 = url + citylink

html2 = requests.get(url2)
# print(html2)
sq2 = BeautifulSoup(html2.text, "html.parser")
# print(sq2)

data = sq2.select(".aqivalue")
print("天津PM2.5的数值为：", data[0].text)
# data = sq2.find("div", {"class": "aqivalue"})
# print(data.text)

# if __name__ == '__main__':
#     pass