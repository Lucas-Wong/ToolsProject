# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-01-29 
"""
from Tkinter import Tk

class Clipboard(object):
    def addToClipboard(self, string):
        """字符串添加到剪贴板"""
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(string)
        r.update()
        r.destroy()

    def getClipboard(self):
        """返回剪贴板上的内容"""
        r = Tk()
        r.withdraw()
        tmp = r.clipboard_get()
        r.destroy()
        return tmp

if __name__ == '__main__':
    Clipboard().addToClipboard("alex lee")
    Clipboard().addToClipboard("alex lee33333")
