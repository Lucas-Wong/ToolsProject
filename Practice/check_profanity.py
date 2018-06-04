#! /usr/bin/env python
#  _*_coding:utf-8_*_

import urllib.request

def read_text():
    quotes = open("D:\CodeWorkspace\python\ToolsProject\Practice\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    # connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q=shot")
    output = connection.read()
    print(output)
    connection.close()

read_text()