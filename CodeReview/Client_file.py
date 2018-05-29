# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-02-06 
"""

import os
import sys
import time

sys.path.append(r'D:\CodeWorkspace\python\GeneralTools')
from File import File_operation
from Log import LogUtils

file_operation = File_operation.File_operation()
file_name_list = ["*.pdb", "iConn.CreateXmlTools.*"]


def remove_master_file():
    """
    File path is master
    :rtype: object
    """
    os.chdir(r"D:\CodeWorkspace\iConnAll\Client-master\iConn.CreateXmlTools\bin\Release")
    print("Current Working Directory is " + os.getcwd())

    file_operation.remove_file(file_name_list)
    file_operation.change_file(r'http://172.16.1.81:8081/UpdateClient/')


def remove_release_file():
    """
    File path is master
    :rtype: object
    """
    os.chdir(r"D:\CodeWorkspace\iConnAll\Client-master\iConn.CreateXmlTools\bin\Release")
    print("Current Working Directory is " + os.getcwd())

    file_operation.remove_file(file_name_list)
    file_operation.change_file(r'http://172.16.1.215:8097/UpdateRelease/')


def remove_dev_file():
    """
    File path is dev
    :rtype: object
    """
    os.chdir(r"D:\CodeWorkspace\iConnAll\Client-dev\iConn.CreateXmlTools\bin\Release")
    print("Current Working Directory is " + os.getcwd())

    file_operation.remove_file(file_name_list)
    file_operation.change_file(r'http://172.16.1.215:8097/UpdateClient/')

    # self.upload_file("172.16.1.215", "tomcat", "tomcat123", file_list, os)


def newco_master_file():
    """
    File path is master
    :rtype: object
    """
    os.chdir(r"D:\CodeWorkspace\NewCo\NewCoClient-master\iConn.CreateXmlTools\bin\Release")
    print("Current Working Directory is " + os.getcwd())

    file_operation.remove_file(file_name_list)
    file_operation.change_file(r'http://172.16.1.162:8097/UpdateClient/')


def newco_release_file():
    """
    File path is master
    :rtype: object
    """
    os.chdir(r"D:\CodeWorkspace\NewCo\NewCoClient-master\iConn.CreateXmlTools\bin\Release")
    print("Current Working Directory is " + os.getcwd())

    file_operation.remove_file(file_name_list)
    file_operation.change_file(r'http://172.16.1.162:8097/UpdateClient/')


def newco_dev_file():
    """
    File path is dev
    :rtype: object
    """
    os.chdir(r"D:\CodeWorkspace\NewCo\NewCoClient-dev\iConn.CreateXmlTools\bin\Release")
    print("Current Working Directory is " + os.getcwd())

    file_operation.remove_file(file_name_list)
    file_operation.change_file(r'http://172.16.1.162:8097/UpdateClient-dev/')


def start_remove():
    """
    This is user input
    :return:
    """
    current_money = 1
    while current_money > 0:
        print('Remove Starts!'.center(50, "#"))
        print('1. Remove Master. \n2. Remove Release. \n3. Remove Dev. ')
        print('11. Remove NewCo Master. \n12. Remove NewCo Release. \n13. Remove NewCo Dev. ')
        print('[Help]: q:quit   clear:clear screen. ')
        print(''.center(50, "#"))
        your_choice = input('Please select : ')
        if your_choice == 1 or your_choice == '1':
            remove_master_file()
        elif your_choice == 2 or your_choice == '2':
            remove_release_file()
        elif your_choice == 3 or your_choice == '3':
            remove_dev_file()
        elif your_choice == 11 or your_choice == '11':
            newco_master_file()
        elif your_choice == 12 or your_choice == '12':
            newco_release_file()
        elif your_choice == 13 or your_choice == '13':
            newco_dev_file()
        elif your_choice == "clear":
            # setting.clear()
            pass
        elif your_choice == "q" or your_choice == "Q" or your_choice == "quit":
            current_money = 0
        else:
            print('Invalid input!')
    else:
        print('Exit!')


if __name__ == '__main__':
    start_remove()