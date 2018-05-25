# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-02-05 
"""

import paramiko
import os
import sys

from bin import setting

path = os.path.dirname(os.path.abspath(sys.argv[0]))

def choose():
    of = open("{}/bin/information.d".format(path))
    hosts = of.readlines()
    hosts_temp = []
    for h in hosts:
        if h.strip():
            hosts_temp.append(h)
    hosts = hosts_temp[:]
    len_host = len(hosts)
    if len_host <= 0:
        setting.clear()
        print("[Warning]Please add the host server")
        return
    while True:
        print('SSH List'.center(50, '='))
        print("+{}+".format("-" * 40))
        print("|     Alias   UserName@IP:PORT")
        for i in range(0, len_host):
            v_list = hosts[i].strip().split(" ")
            print("+{}+".format("-" * 40))
            print("| {} | {}   {}@{}:{}".format(i + 1, v_list[4], v_list[0], v_list[1], v_list[2]))
        print("+{}+".format("-" * 40))
        c = input("[SSH]Choose the number or alias('#q' exit):")
        is_alias = False
        is_y = False
        try:
            c = int(c)
            if c > len_host or c < 1:
                setting.clear()
                print("[Warning]:There is no")
                continue
            l_list = hosts[c - 1].split(" ")
            name = l_list[0]
            host = l_list[1]
            port = l_list[2]
            password = l_list[3]
            is_y = True
        except:
            is_alias = True

        if is_alias:
            if c.strip() == "#q":
                setting.clear()
                return
            for h in hosts:
                if c.strip() == h.split(" ")[4].strip():
                    l_list = h.split(" ")
                    name = l_list[0]
                    host = l_list[1]
                    port = l_list[2]
                    password = l_list[3]
                    is_y = True

        if not is_y:
            continue

        print("In the connection...")
        print("{}@{}".format(name, host))
        while True:
            print("SSH [Menu]".center(40, '='))
            print("1.Exec command\n2.Upload file\n3.Down file\n[Help]: q:quit   clear:clear screen")
            print("=".center(40, '='))
            c = input("Please select :")
            if c == 1 or c == "1":
                exec_command(host, port, name, password)
            if c == 2 or c == "2":
                print("功能未实现")
            if c == 3 or c == "3":
                print("功能未实现")
            elif c == "clear":
                setting.clear()
            elif c == "q" or c == "Q" or c == "quit":
                break
            else:
                print("\n")

def exec_command(host, port, name, password):
    print("SSH [Menu]".center(40, '='))
    print("Please input command[Help]: q:quit   clear:clear screen")
    print("=".center(40, '='))
    c = input("Please select :")
    if c == "clear":
        setting.clear()
    elif c == "q" or c == "Q" or c == "quit":
        return
    else:
        ssh = SSHConnection(host, port, name, password)
        ssh.connect()
        r1 = ssh.cmd(str(c))
        print(r1.decode())

        ssh.close()

class SSHConnection(object):

    def __init__(self, host='172.16.1.215', port=22, username='tomcat', pwd='tomcat123'):
        self.host = host
        self.port = port
        self.username = username
        self.pwd = pwd
        self.__k = None

    def run(self):
        self.connect()
        pass
        self.close()

    def connect(self):
        transport = paramiko.Transport(self.host, self.port)
        transport.connect(username=self.username, password=self.pwd)
        self.__transport = transport

    def close(self):
        self.__transport.close()

    def cmd(self, command):
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command)
        # 获取命令结果
        result = stdout.read()
        return result

    def upload(self, local_path, target_path):
        # 连接，上传
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        # 将location.py 上传至服务器 /tmp/test.py
        sftp.put(local_path, target_path)

if __name__ == '__main__':
    ssh = SSHConnection()
    ssh.connect()
    r1 = ssh.cmd('df')
    print(r1.decode())
    ssh.upload('class12.py', "test.py")
    ssh.close()