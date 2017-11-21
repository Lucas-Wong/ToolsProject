#! /usr/bin/env python
# _*_ coding:utf-8 _*_

def data_year(data_string):
    if (data_string % 400 == 0) or ((data_string % 4 == 0) and (data_string % 100 != 0)):
        print(u"%d 是闰年" % data_string)
    else:
        print(u"%d 不是闰年" % data_string)


if __name__ == "__main__":
    data_string = int(input("Please input year:"))
    data_year(data_string)
