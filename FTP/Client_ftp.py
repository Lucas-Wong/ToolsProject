# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-02-02
DESC:FTP上传功能
"""

import os, ftplib
import time, socket





nonpassive = False
remotesite = "172.16.1.215"
remoteport = 22
remotedir  = "/home/tomcat/deployment/apache-tomcat-7.0.47-ic/webapps/UpdateClient"
remoteuser = "tomcat"
remotepass = "tomcat123"
localdir   = r'D:\\CodeWorkspace\\iConnAll\\Client-dev\\iConn.CreateXmlTools\\bin\\Release'



print(">>正在连接FTP....<<")
conn = ftplib.FTP()
##连接建立环节
try:
    conn.connect(remotesite, remoteport)
except socket.error:
    print(">>远程FTP服务器出现异常，连接失败，5秒后重连！<<")
    try:
        time.sleep(5)
        conn.connect(remotesite,remoteport)
    except socket.error:
        pass
    finally:
        print(">>重连失败，退出连接，请检查远程FTP服务器！<<")
        exit()



##登陆
conn.login(remoteuser, remotepass)
##切换远程工作目录
conn.cwd(remotedir)

if nonpassive:
    conn.set_pasv(False)
#成功上传数
succeed_count = 0
#重传位置
retrans_positions = 0
#重传位置列表
retrans_list  = []


#获取本地目录下所有的文件信息，并返回一个列表
localfile_list = os.listdir(localdir)

#文件总数
filecounts = len(localfile_list)


# 上传开始时间
startput_time = time.strftime("%H:%M:%S")

for localname in localfile_list:
    localpath = os.path.join(localdir, localname)

    print(">>正在上传,StartTime:%s<< " % startput_time, localpath, localname)
    #ascii模式和字节文件进行传输，ftplib的回车换行逻辑要求使用rb模式
    localfile = open(localpath, 'rb')
    try:
        conn.storlines("STOR " + localname, localfile)
        localfile.close()
        succeed_count += 1

    #传输异常中断
    except ftplib.error_temp:
        retrans_positions = (succeed_count + 1)
        retrans_list.append(retrans_positions)
        print(">>发生传输异常中断，时间为:%s<<" % time.strftime("%H:%M:%S"))
        #异常中断后进行重连
        conn.connect(remotesite, remoteport)
        conn.login(remoteuser, remotepass)
        conn.cwd(remotedir)
        continue


#上传结束时间
endput_time = time.strftime("%H:%M:%S")
conn.quit()
#总耗时
#totalput_time = (endput_time - startput_time)
print(">>开始时间：%s; 结束时间：%s <<" % (startput_time, endput_time))
print(">>文件总数：%s 成功上传:%s 重传次数:%s 重传开始位置：%s  <<" % (filecounts, succeed_count, len(retrans_list), len(retrans_list) or "Null"))