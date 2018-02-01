# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-01-21 
"""
import logging
import time
import logging.handlers

rq = time.strftime('%Y%m%d', time.localtime(time.time()))


class Log(object):
    """
    日志类
    """
    def __init__(self, name):
        self.path = "/User/aaa/log/"  # 定义日志存放路径
        self.filename = self.path + rq + '.log'  # 日志文件名称
        self.name = name  # 为%(name)s赋值
        self.logger = logging.getLogger(self.name)
        # 控制日志文件中记录级别
        self.logger.setLevel(logging.INFO)
        # 控制输出到控制台日志格式、级别
        self.ch = logging.StreamHandler()
        gs = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s[line:%(lineno)d] - %(message)s')
        self.ch.setFormatter(gs)
        # self.ch.setLevel(logging.NOTSET)    写这个的目的是为了能控制控制台的日志输出级别，但是实际中不生效，不知道为啥，留着待解决
        # 日志保留10天,一天保存一个文件
        self.fh = logging.handlers.TimedRotatingFileHandler(self.filename, 'D', 1, 10)
        # 定义日志文件中格式
        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s -   %(name)s[line:%(lineno)d] - %(message)s')
        self.fh.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)


class customError(Exception):
    """
    自定义异常类,用在主动输出异常时使用,用 raise关键字配合使用,例:
          if True:
                pass
          else:
                raise customError(msg)
    """

    def __init__(self, msg=None):
        self.msg = msg

    def __str__(self):
        if self.msg:
            return self.msg
        else:
            return u"某个不符合条件的语法出问题了"

class Log2:
    # 日志文件名称
    __file = 'log.log'
    __handler = False
    # 输出格式
    __fmt = '%(asctime)s - %(filename)s:[line:%(lineno)s] - %(name)s - %(message)s'

    def __init__(self):
        logging.basicConfig(filename=self.__file, filemode='a+', format=self.__fmt)
        # self.__handler = logging.handlers.RotatingFileHandler(self.__file, maxBytes=1024*1024, backupCount=5)
        # 打印
        self.__handler = logging.StreamHandler()
        self.__handler.setLevel(logging.INFO)

        # 设置格式
        formatter = logging.Formatter(self.__fmt)
        self.__handler.setFormatter(formatter)
        return

    # 获取实例
    def getInstance(self, strname):
        logger = logging.getLogger(strname)
        logger.addHandler(self.__handler)
        logger.setLevel(logging.DEBUG)
        return logger

if __name__ == '__main__':
    """
from Function.Log_main_class import *
try:
   log = Log("casename")
   log.info("msg")
   if True:                
           pass
   else:
           raise customError(msg)
except BaseException as msg:
   log.exception(msg)
    """

    testlog = Log2().getInstance("test")
    testlog.info("info log")
    testlog.debug("debug log")
    testlog.warning("waring log")

