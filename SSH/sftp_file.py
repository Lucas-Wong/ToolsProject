# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-02-04 
"""
import paramiko

print("0".center(50, '='))
ssh = paramiko.Transport(r"172.16.1.215", 22)
print("1".center(50, '='))
ssh.connect(username="tomcat", password="tomcat123")
print("2".center(50, '='))
sftp = paramiko.SFTPClient.from_transport(ssh)
print("3".center(50, '='))
local_file = "crucible.py"
remote_file = "crucible.py"
try:
  print("4".center(50, '='))
  sftp.put(local_file, remote_file)
  print("5".center(50, '='))
except Exception as es:
    print("[-]put Error:User name or password error or uploaded file does not exist")
    print(es)


print("上传")
ssh.close()

if __name__ == '__main__':
    pass