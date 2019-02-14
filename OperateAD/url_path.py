# -*- coding: utf-8 -*-
"""
-----------------------------------------------------
    File Name:        url_path
    Author:           Lucas.wang
    Date:             2019-02-06 17:10
    Description:      
-----------------------------------------------------
    Change Activity:  2019-02-06 17:10
    Description:      
----------------------------------------------------
"""

class url_path(object):

    def __init__(self):
        pass

    def rtn_url(self, company, version):
        if str("ARIIX") == company:
            if str("release") == version:
                return self.ariix_release()
            elif str("live") == version:
                return self.ariix_live()
            else:
                return self.ariix_dev()
        elif str("MAVIE") == company:
            if str("release") == version:
                return self.mavie_release()
            elif str("live") == version:
                return self.mavie_live()
            else:
                return self.mavie_dev()

    # @staticmethod
    def ariix_release(self):
        """
        Release url
        :return:
        """
        return "http://172.16.1.195:8097/iConn/iconnHandler.do"

    # @staticmethod
    def ariix_live(self):
        """
        Live url
        :return:
        """
        return "http://172.16.1.83:8097/iConn/iconnHandler.do"

    def ariix_dev(self):
        """
        Dev url
        :return:
        """
        return "http://172.16.1.197:8097/iConn/iconnHandler.do"

    # @staticmethod
    def mavie_dev(self):
        """
        Dev url
        :return:
        """
        return "http://172.16.1.162:8097/iConn/iconnHandler.do"

    # @staticmethod
    def mavie_release(self):
        """
        Release url
        :return:
        """
        return "http://172.16.1.163:8097/iConn/iconnHandler.do"

    # @staticmethod
    def mavie_live(self):
        """
        Dev url
        :return:
        """
        return "http://172.16.1.166:8097/iConn/iconnHandler.do"

if __name__ == '__main__':
    path = url_path()
    print(path.rtn_url("ARIIX", "dev"))