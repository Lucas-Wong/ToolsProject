# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-02-06 
"""

import glob
import os

def remove_file(file_name_list):
    print("glob remove file".center(50, "="))
    print("Current Working Directory is " + os.getcwd())
    files = []
    for file_name in file_name_list:
        files += glob.glob(file_name)
    # print(files)
    # files = glob.glob("*.pdb") + glob.glob("iConn.CreateXmlTools.*")
    for file in files:
        try:
            os.remove(file)
        except IOError:
            print(file + " don't delete")
        else:
            print(file)
    print("glob remove file".center(50, "="))

if __name__ == '__main__':
    pass