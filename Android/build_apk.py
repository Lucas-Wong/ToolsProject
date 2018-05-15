# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-01-12 
"""
import os
import time
import smtplib
from email.mime.text import MIMEText

mailto_list = ['xxoo.qin@fantasee.cn','xx@fantasee.cn','oo@fantasee.cn']
mail_host = "smtp.163.com" # 设置服务器
mail_user = "xianyin0@163.com" # 用户名
mail_pass = "5213344" # 口令
def send_mail(to_list, sub, content):#有错误发送邮件
    me='xianyin0@163.com'
    msg = MIMEText(content, format, 'utf-8')
    msg["Accept-Language"] = "zh-CN"
    msg["Accept-Charset"] = "utf-8"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ",".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
    except Exception as e:
        print(str(e))

def logger(content):#记录日志
    date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    with open('/root/log.txt','a') as f:
        f.write('[%s]:%s\n'%(date,content))

def yunpos2():#yunpos2打包apk代码
    os.chdir(r'/usr/local/yunpos2/pos/yunpos')
    content=os.popen('svn up')
    data = content.read()
    if len(data)>50:
        try:
            data0=os.popen(r'gradle aR')
            os.chdir(r'/usr/local/yunpos2/pos/yunpos/app/build/outputs/apk/')
            data2 = os.popen('ls')
            for i in data2.readlines():
                pass
            date2 = i.split('_',4)[0] + '_' + i.split('_',4)[1] + '_' + i.split('_',4)[2] + '_' + i.split('_',4)[3]
            os.system(r'zip -r /var/ftp/apk/%s.zip yunpos2*.apk'%date2)
            os.system('rm -rf yunpos2*.apk')
        except:
            logger('yunpos2打包失败')
            send_mail(mailto_list, "yunpos2 packaging failure",data)
    else:
        logger('yunpos2代码没有更新')

def possdk():#possdk打包apk代码
    os.chdir(r'/usr/local/yunpos2/pos/possdk')
    content=os.popen('svn up')
    data = content.read()
    if len(data)>50:
        try:
            os.system(r'gradle aR')
            os.chdir(r'/usr/local/yunpos2/pos/possdk/app/build/outputs/apk')
            data2 = os.popen('ls')
            for i in data2.readlines():
                date2 = i.split('_',4)[0] + '_' + i.split('_',4)[1] + '_' + i.split('_',4)[2] + '_' + i.split('_',4)[3]
                break
            os.system(r'zip -r /var/ftp/apk/%s.zip yunpos*.apk'%date2)
            os.system('rm -rf yunpos*.apk')
        except:
            logger('possdk打包失败')
            send_mail(mailto_list, "possdk packaging failure",data)
    else:
        logger('possdk代码没有更新')

def yunpos():#yunpos打包apk代码
    os.chdir(r'/usr/local/yunpos/android/yunpos')
    content=os.popen('svn up')
    data = content.read()
    if len(data)>50:
        try:
            os.system(r'gradle aR')
            os.chdir(r'/usr/local/yunpos/android/yunpos/build/outputs/apk')
            data2 = os.popen('ls')
            for i in data2.readlines():
                date2 = i.split('_',4)[0] + '_' + i.split('_',4)[1] + '_' + i.split('_',4)[2] + '_' + i.split('_',4)[3]
                break
            os.system(r'zip -r /var/ftp/apk/%s.zip yunpos*.apk'%date2)
            os.system('rm -rf yunpos*.apk')
        except:
            logger('yunpos打包失败')
            send_mail(mailto_list, "yunpos packaging failure",data)
    else:
        logger('yunpos代码没有更新')

if __name__ == '__main__':
    yunpos2()
    possdk()
    yunpos()