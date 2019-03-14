# -*- coding: utf-8 -*-
"""
-----------------------------------------------------
    File Name:        TxtFile
    Author:           Lucas.wang
    Date:             2019-03-06 9:48
    Description:      
-----------------------------------------------------
    Change Activity:  2019-03-06 9:48
    Description:      
----------------------------------------------------
"""
import os

import numpy as np


class operate_file(object):

    pos = []
    Efield = []

    def read_file(self, read_file_path):
        files = open(read_file_path, "r", encoding='utf-8')
        return files

    def write_file(self, write_file_path):
        files = open(write_file_path, "w", encoding='utf-8')
        for str in self.Efield:
            files.write(str)
        files.close()
        # return files

    def operateTxtFile(self, file_path, write_file_path):
        txt_file = self.read_file(file_path)
        # with txt_file as file_to_read:
        #     while True:
        #         lines = file_to_read.readline()
        #         if not lines:
        #             break
        #         p_tmp, E_tmp = [float(i) for i in lines.split('("')]
        #
        #         self.pos.append(p_tmp)  # 添加新读取的数据
        #         self.Efield.append(E_tmp)
        #     self.pos = np.array(self.pos)  # 将数据从list类型转换为array类型。
        #     self.Efield = np.array(self.Efield)
        with txt_file as read_f:  # 同时打开文件
            for line in read_f:  # 循环原文件内容
                str1 = line.split("(\"")[-1]
                str2 = str1.replace("\",\"", " = ")
                self.Efield.append(str1)
        self.write_file(write_file_path)



if __name__ == '__main__':
    op = operate_file()
    op.operateTxtFile("errorCode.txt", "error.txt")