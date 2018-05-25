# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
方便在LINUX终端使用ssh,保存使用的IP:PORT , PASSWORD
自动登录
@author = lucas.wang 
@create_time = 2018-02-05 
"""

import os
import sys
import platform

from bin import setting
from bin import auto_ssh

sys.path.append("../")

path = os.path.dirname(os.path.abspath(sys.argv[0]))


def main():
    while 1:

        print("SSH [Menu]".center(40, '='))
        print("1.Connection between a host\n2.Add host\n3.Remove host\n4.About\n[Help]: q:quit   clear:clear screen")
        print("=".center(40, '='))
        c = input("Please select :")
        if c == 1 or c == "1":
            auto_ssh.choose()
        if c == 2 or c == "2":
            # setting.add_host_main()
            print("功能未实现")
        if c == 3 or c == "3":
            # setting.remove_host()
            print("功能未实现")
        if c == 4 or c == "4":
            setting.about()
        elif c == "clear":
            setting.clear()
        elif c == "q" or c == "Q" or c == "quit":
            print("System edit. Bye")
            sys.exit()
        else:
            print("\n")


if __name__ == '__main__':
    try:
        of = open("{}/bin/information.d".format(path))
    except:
        of = open("{}/bin/information.d".format(path), "w")
    of.close()

    main()
