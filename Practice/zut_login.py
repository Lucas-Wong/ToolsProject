#! /usr/bin/env python
# _*_coding:utf-8_*_

import requests
import socket
localIP = socket.gethostbyname(socket.gethostname())
# ip list
ipList = socket.gethostbyname_ex(socket.gethostname())
ip = ipList[2][0]
# //构造url
url = 'http://1.1.1.1:801/eportal/?c=ACSetting&a=Login' \
      '&protocol=http:&hostname=1.1.1.1&iTermType=1' \
      '&wlanuserip=' + ip +'&wlanacip=null&wlanacname=null' \
                           '&mac=00-00-00-00-00-00&ip=' + ip + '&enAdvert=0&queryACIP=0&loginMethod=1'
# //post数据
postdata = {
'DDDDD':'201508030117',
'upass':'186819',
'R1':'0',
'R2':'0',
'R3':'0',
'R6':'0',
'para':'00',
'0MKKey':'123456',
}
a=requests.post(url,postdata)
print('登陆成功！')

