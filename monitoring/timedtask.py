# _*_ coding:utf-8 _*_
"""
-----------------------------------------------------------
 Name：            ToolsProject/timedtask
 Purpose：         

 Author：          lucas.wang

 Created：         2018-08-23
 Copyright：       (C) lucas.wang 2018
 Licence:          MIT
 ----------------------------------------------------------
"""
# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/27 15:59
# @Desc    : 定时任务，以需要的时间间隔执行某个命令
# @File    : timedtask.py
# @Software: PyCharm

import time, os
from monitorserver import alltask


def roll_back(cmd, inc=60):
    while True:
        # 执行方法，函数
        alltask()
        time.sleep(inc)


roll_back("echo %time%", 5)


if __name__ == '__main__':
    pass