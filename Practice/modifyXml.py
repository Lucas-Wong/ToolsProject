#! /usr/bin/env python
# _*_coding:utf-8_*_

# 用于 Clinet 端升级失败，改写 config 文件， 可以再次升级
import os
from xml.etree.ElementTree import ElementTree, Element
import time

def read_xml (in_path):
    tree = ElementTree()
    tree.parse(in_path)
    return tree

def write_xml (tree, out_path):
    tree.write(out_path, encoding="utf-8", xml_declaration=True)

def modify_autoupdate_service_live ():
    tree = read_xml(os.getcwd() + "/Autoupdater.config")

    root = tree.getroot()

    for item in root.iter("ServerUrl"):
        item.text = "http://172.16.1.81:8081/UpdateClient/AutoupdateService.xml"

    write_xml(tree, os.getcwd() + "/Autoupdater.config")

def modify_autoupdate_service_dev ():
    tree = read_xml(os.getcwd() + "/Autoupdater.config")

    root = tree.getroot()

    for item in root.iter("ServerUrl"):
        item.text = "http://172.16.1.215:8097/UpdateClient/AutoupdateService.xml"

    write_xml(tree, os.getcwd() + "/Autoupdater.config")

def modify_autoupdate_version ():
    tree = read_xml(os.getcwd() + "/Autoupdater.config")

    root = tree.getroot()

    for item in root.iter("LocalFile"):
        item.set("version", "")

    write_xml(tree, os.getcwd() + "/Autoupdater.config")

def sleep_second(seconds=1):
    '''休眠'''
    time.sleep(seconds)

def state_modify():
    current_money = 1
    sleep_second()
    while current_money > 0:
        print('<<<<<<<<<<<<<<<<<<<< Toole Starts! >>>>>>>>>>>>>>>>>>>>')
        print('1. Modify config file，用于再次升级 client 端。')
        print('2. Modify config file，用于修改访问 Live 服务器的接口。')
        print('3. Modify config file，用于修改访问 Dev 服务器的接口。')
        print('4. Exit。')
        your_choice = input('请输入 1 / 2 / 3 / 4 : ')
        choices = ['1','2','3','4']
        if your_choice in choices:
            if your_choice == '1':
                modify_autoupdate_version()
            if your_choice == '2':
                modify_autoupdate_service_live()
            if your_choice == '3':
                modify_autoupdate_service_dev()
            if your_choice == '4':
                current_money = 0
        else:
            print('Invalid input!')
    else:
        sleep_second()
        print('Exit!')
        sleep_second(2)

#if __name__ == "__main__":
state_modify()