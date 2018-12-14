# _*_ coding:utf-8 _*_
"""
-----------------------------------------------------------
 Name：            ToolsProject/download
 Purpose：         

 Author：          lucas.wang

 Created：         2018-08-03
 Copyright：       (C) lucas.wang 2018
 Licence:          MIT
 ----------------------------------------------------------
"""
# ! /usr/bin/env python
import paramiko
import os
from configparser import ConfigParser


# 读取配置文件获取服务器的登录信息
def read_ini():
    info = dict()
    cf = ConfigParser()
    cf.read('config.ini', encoding='utf-8')
    keys = cf.options('ssh')
    for each in keys:
        info[each] = cf.get('ssh', each)
    print(info)
    return info

def read_cmd_ini(title):
    cmd_info = dict()
    cf = ConfigParser()
    cf.read('config.ini', encoding='utf-8')
    keys = cf.options(title)
    for each in keys:
        cmd_info[each] = cf.get(title, each)

    return cmd_info

# 连接服务区并执行shell命令返回输出结果
def ssh_test(host, port, username, password, title):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    try:
        ssh.connect(hostname=host, port=port, username=username, password=password)
    except Exception as e:
        print(e)
        return

    # 设置一个内部函数，执行shell命令并返回输出结果
    def run_shell(cmd):
        ssh_in, ssh_out, ssh_error = ssh.exec_command(cmd)
        result = ssh_out.read() or ssh_error.read()
        return result.decode().strip()

    cmd_info = read_cmd_ini(title)

    # 获取指定文件夹的绝对地址
    # cmd_get_path = 'cd logs;pwd' # logs
    # cmd_get_path = 'cd deployment/apache-tomcat-7.0.47-ic/webapps/UpdateClient/ ; pwd'
    cmd_get_path = cmd_info.get('pwd', None)
    db_path = run_shell(cmd_get_path)

    # 获取指定文件夹中文件的名称，并跟上面得到的文件夹绝对地址组合起来
    # cmd_get_sqls = 'cd logs;ls' # logs
    # cmd_get_sqls = "cd deployment/apache-tomcat-7.0.47-ic/webapps/UpdateClient/; ls"
    cmd_get_sqls = cmd_info.get('ls', None)
    sqls = run_shell(cmd_get_sqls)
    lis = ['{}/{}'.format(db_path, each) for each in sqls.split('\n')]
    print(lis)

    # 关闭连接
    ssh.close()
    return lis


# 链接服务器进行文件传输
def sftp_test(host, port, username, password, from_file, to_file):
    transport = paramiko.Transport((host, port))
    try:
        transport.connect(username=username, password=password)
    except Exception as e:
        print(e)
        return
    sftp = paramiko.SFTPClient.from_transport(transport)

    # 将文件下载到本地，如果是上传使用 put
    sftp.get(from_file, to_file)
    transport.close()


if __name__ == '__main__':
    info = read_ini()
    h = info.get('host', None)
    p = int(info.get('port', None)) # 端口是int类型
    u = info.get('username', None)
    pw = info.get('password', None)
    files = ssh_test(h, p, u, pw, 'backiConn')

    path = 'D:\\dbs'
    if files:
        for each in files:
            name = each.split('/')[-1]
            ss = sftp_test(h, p, u, pw, each, os.path.join(path, name))