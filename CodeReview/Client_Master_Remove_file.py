#! /usr/bin/env python
# _*_coding:utf-8_*_

import os
import sys
import time

import Remove_file
from Change_Xml import change_xml as update_xml

sys.path.append(r'D:\CodeWorkspace\python\GeneralTools')
from File import File_operation

# 用于删除client生成时不需要的文件的工具，file path 是client 端tools 的生成目录
class Remove(object):
    """
    Remove file use
    Tools for deleting files that are not needed for client generation,
        and file path is the generation directory for client-side tools.
    """

    file_name_list = ["*.pdb", "iConn.CreateXmlTools.*"]
    # @staticmethod
    # def remove_file():
    #     """
    #     Base function, Remove file
    #     :return:
    #     """
    #     print("glob".center(50, "="))
    #     files = glob.glob("*.pdb") + glob.glob("iConn.CreateXmlTools.*")
    #     for file in files:
    #         try:
    #             os.remove(file)
    #         except IOError:
    #             print(file + " don't delete")
    #         else:
    #             print(file)
    #     print("glob".center(50, "="))

    # @staticmethod
    # def remove_file(file_list, os_file):
    #     """
    #     Base function, Remove file
    #     :param file_list:
    #     :param os_file:
    #     :return:
    #     """
    #     for file_name in file_list:
    #         # if file_name[-3:] == 'pdb':
    #         if os.path.exists(file_name):
    #             if os_file.path.splitext(file_name)[1] == '.pdb':
    #                 print(file_name)
    #                 os_file.remove(file_name)
    #
    #             if fnmatch.fnmatch(file_name, 'iConn.CreateXmlTools.*'):
    #                 try:
    #                     os_file.remove(file_name)
    #                 except IOError:
    #                     print(file_name + " don't delete")
    #                 else:
    #                     print(file_name)


    def remove_master_file(self):
        """
        File path is master
        :rtype: object
        """
        # file_list = os.listdir(r'D:\CodeWorkspace\iConnAll\Client-master\iConn.CreateXmlTools\bin\Release')
        # print(file_list)
        # saved_path = os.getcwd()
        # print("Current Working Directory is " + saved_path)
        os.chdir(r"D:\CodeWorkspace\iConnAll\Client-master\iConn.CreateXmlTools\bin\Release")
        print("Current Working Directory is " + os.getcwd())
        # self.remove_file(file_list, os)
        # Remove_file.remove_file(self.file_name_list)
        #
        # update = update_xml(r'http://172.16.1.81:8081/UpdateClient/', os.getcwd().strip() + "\\")
        # update.read_xml()

        file_operation = File_operation.File_operation()
        file_operation.remove_file(self.file_name_list)
        file_operation.change_file("xml", "AutoupdateService", r'http://172.16.1.81:8081/UpdateClient/')

    def remove_release_file(self):
        """
        File path is master
        :rtype: object
        """
        # file_list = os.listdir(r'D:\CodeWorkspace\iConnAll\Client-master\iConn.CreateXmlTools\bin\Release')
        # print(file_list)
        # saved_path = os.getcwd()
        # print("Current Working Directory is " + saved_path)
        os.chdir(r"D:\CodeWorkspace\iConnAll\Client-master\iConn.CreateXmlTools\bin\Release")
        print("Current Working Directory is " + os.getcwd())
        # self.remove_file(file_list, os)
        # Remove_file.remove_file(self.file_name_list)
        #
        # update = update_xml(r'http://172.16.1.215:8097/UpdateRelease/', os.getcwd().strip() + "\\")
        # update.read_xml()

        file_operation = File_operation.File_operation()
        file_operation.remove_file(self.file_name_list)
        file_operation.change_file("xml", "AutoupdateService", r'http://172.16.1.215:8097/UpdateRelease/')


    def remove_dev_file(self):
        """
        File path is dev
        :rtype: object
        """
        # file_list = os.listdir(r'D:\CodeWorkspace\iConnAll\Client-dev\iConn.CreateXmlTools\bin\Release')
        # print(file_list)
        # saved_path = os.getcwd()
        # print("Current Working Directory is " + saved_path)
        os.chdir(r"D:\CodeWorkspace\iConnAll\Client-dev\iConn.CreateXmlTools\bin\Release")
        print("Current Working Directory is " + os.getcwd())

        # self.remove_file(file_list, os)
        # Remove_file.remove_file(self.file_name_list)

        # update = update_xml(r'http://172.16.1.215:8097/UpdateClient/', os.getcwd().strip() + os.sep)
        # update.read_xml()

        file_operation = File_operation.File_operation()
        file_operation.remove_file(self.file_name_list)
        file_operation.change_file("xml", "AutoupdateService", r'http://172.16.1.215:8097/UpdateClient/')

        # self.upload_file("172.16.1.215", "tomcat", "tomcat123", file_list, os)

    def newco_master_file(self):
        """
        File path is master
        :rtype: object
        """
        # file_list = os.listdir(r'D:\CodeWorkspace\NewCo\NewCoClient-master\iConn.CreateXmlTools\bin\Release')
        # print(file_list)
        # saved_path = os.getcwd()
        # print("Current Working Directory is " + saved_path)
        os.chdir(r"D:\CodeWorkspace\NewCo\NewCoClient-master\iConn.CreateXmlTools\bin\Release")
        print("Current Working Directory is " + os.getcwd())
        # self.remove_file(file_list, os)
        # Remove_file.remove_file(self.file_name_list)
        #
        # update = update_xml(r'http://172.16.1.163:8097/UpdateClient/', os.getcwd().strip() + "\\")
        # update.read_xml()

        file_operation = File_operation.File_operation()
        file_operation.remove_file(self.file_name_list)
        file_operation.change_file("xml", "AutoupdateService", r'http://172.16.1.163:8097/UpdateClient/')

    def newco_release_file(self):
        """
        File path is master
        :rtype: object
        """
        # file_list = os.listdir(r'D:\CodeWorkspace\NewCo\NewCoClient-master\iConn.CreateXmlTools\bin\Release')
        # print(file_list)
        # saved_path = os.getcwd()
        # print("Current Working Directory is " + saved_path)
        os.chdir(r"D:\CodeWorkspace\NewCo\NewCoClient-master\iConn.CreateXmlTools\bin\Release")
        print("Current Working Directory is " + os.getcwd())
        # self.remove_file(file_list, os)
        # Remove_file.remove_file(self.file_name_list)
        #
        # update = update_xml(r'http://172.16.1.163:8097/UpdateClient/', os.getcwd().strip() + "\\")
        # update.read_xml()

        file_operation = File_operation.File_operation()
        file_operation.remove_file(self.file_name_list)
        file_operation.change_file("xml", "AutoupdateService", r'http://172.16.1.163:8097/UpdateClient/')

    def newco_dev_file(self):
        """
        File path is dev
        :rtype: object
        """
        # file_list = os.listdir(r'D:\CodeWorkspace\NewCo\NewCoClient-dev\iConn.CreateXmlTools\bin\Release')
        # print(file_list)
        # saved_path = os.getcwd()
        # print("Current Working Directory is " + saved_path)
        os.chdir(r"D:\CodeWorkspace\NewCo\NewCoClient-dev\iConn.CreateXmlTools\bin\Release")
        print("Current Working Directory is " + os.getcwd())
        # self.remove_file(file_list, os)
        # Remove_file.remove_file(self.file_name_list)
        #
        # update = update_xml(r'http://172.16.1.162:8097/UpdateClient/', os.getcwd().strip() + "\\")
        # update.read_xml()

        file_operation = File_operation.File_operation()
        file_operation.remove_file(self.file_name_list)
        file_operation.change_file("xml", "AutoupdateService", r'http://172.16.1.162:8097/UpdateClient/')

    @staticmethod
    def sleep_second(seconds=1):
        """sleep"""
        time.sleep(seconds)

    def start_remove(self):
        """
        This is user input
        :return:
        """
        current_money = 1
        self.sleep_second()
        while current_money > 0:
            print('<<<<<<<<<<<<<<<<<<<< Remove Starts! >>>>>>>>>>>>>>>>>>>>')
            print('1. Remove Master. ')
            print('2. Remove Release. ')
            print('3. Remove Dev. ')
            print('11. Remove NewCo Master. ')
            print('12. Remove NewCo Release. ')
            print('13. Remove NewCo Dev. ')
            print('[Help]: q:quit   clear:clear screen. ')
            your_choice = input('Please select : ')
            if your_choice == 1 or your_choice == '1':
                self.remove_master_file()
            elif your_choice == 2 or your_choice == '2':
                self.remove_release_file()
            elif your_choice == 3 or your_choice == '3':
                self.remove_dev_file()
            elif your_choice == 11 or your_choice == '11':
                self.newco_master_file()
            elif your_choice == 12 or your_choice == '12':
                self.newco_release_file()
            elif your_choice == 13 or your_choice == '13':
                self.newco_dev_file()
            elif your_choice == "clear":
                # setting.clear()
                pass
            elif your_choice == "q" or your_choice == "Q" or your_choice == "quit":
                current_money = 0
            else:
                print('Invalid input!')
        else:
            self.sleep_second()
            print('Exit!')
            self.sleep_second(2)

if __name__ == '__main__':
    remove = Remove()
    remove.start_remove()
