# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-01-12 
"""
import kivy

kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.button import Button


class test(App):
    def build(self):
        return Button(text='hello world')


if __name__ == '__main__':
    test().run()