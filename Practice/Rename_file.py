#! /usr/bin/env python
# _*_coding:utf-8_*_

import os


def rename_files():
    """
    :return:
    """
    file_list = os.listdir(r"D:\CodeWorkspace\python\ToolsProject\Practice\prank")
    # print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir(r"D:\CodeWorkspace\python\ToolsProject\Practice\prank")
    ina = "0123456789"
    outta = "          "
    tantra = str.maketrans(ina, outta)

    for file_name in file_list:
        print("Old Name = " + file_name)
        print("New Name = " + file_name.translate(tantra).strip())
        os.rename(file_name, file_name.translate(tantra).strip())
    os.chdir(saved_path)


rename_files()
