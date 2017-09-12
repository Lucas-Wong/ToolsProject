#! /usr/bin/env python
# _*_coding:utf-8_*_
import time
import webbrowser

#学习 python ， 定时打开网页，可以用于提醒休息
total_breaks = 7
break_count = 0

print("This program started on " + time.ctime())
while break_count < total_breaks:
    time.sleep(30 * 60)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    break_count += 1
