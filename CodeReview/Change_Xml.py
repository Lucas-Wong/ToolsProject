# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-01-12 
"""

from xml.etree import ElementTree as ET
import fnmatch

class change_xml(object):
    """
    xml main function
    """

    names = ['iConn.CreateXmlTools.vshost.exe', 'AutoUpdater.dll', 'NewTonsoft.Json.dll',
             'Oracle.ManagedDataAccess.dll', 'Renci.SshNet.dll', 'Renci.SshNet.xml', 'zxing.dll', 'Images/ARX_HK.png']

    old_path_name = r"http://172.16.1.81:8081/UpdateClient/"

    def __init__(self, path_name, file_path, file_name="AutoupdateService.xml"):
        """
        Init file path name
        :param fileName:
        """
        self.file_path = file_path
        self.file_name = file_name
        self.tree = ET.parse(file_path + file_name)
        self.path_name = path_name

    def read_xml(self):
        """
        Read xml file
        :return:
        """
        root = self.tree.getroot()
        print(root)
        for item in root.getchildren():
            # root.iter("file"):
            print(item.get("url"))

            item.set("url", item.get('url').replace(self.old_path_name, self.path_name))

            if fnmatch.filter(self.names, item.get('path')):
                root.remove(item)

        self.write_xml()

    def write_xml(self):
        self.tree.write(self.file_path + self.file_name)

if __name__ == '__main__':
    """
    Test use
    """
    read = change_xml(r'http://172.16.1.81:8081/UpdateClient/',
                          r'D:\\CodeWorkspace\\iConnAll\\Client-dev\\iConn.CreateXmlTools\\bin\\Release\\')
    read.read_xml()