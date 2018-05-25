# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-02-05 
"""

import re, base64, os, sys, getpass
import platform

# path = os.path.dirname(os.path.abspath(sys.argv[0]))
path = os.path.dirname(__file__)
about_file = "about.dat"

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system("clear")

def about():
    # of = open("{}/bin/about.dat".format(path))
    of = open(os.path.join(path + "\\" + about_file))
    rf = of.read()
    try:
        info = eval(rf)
        clear()
        print("About SSH".center(50, "="))
        for k, v in info.items():
            print("{}: {}".format(k, v))
    except:
        print("For failure.")
    return


if __name__ == '__main__':
    pass