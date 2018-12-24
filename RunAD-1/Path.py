# ! /usr/bin/env python
# _*_ coding:utf-8 _*_

class Path(object):
    """
    Path
    """
    def __init__(self):
        pass

    @staticmethod
    def dev():
        """
        Dev url
        :return:
        """
        return "http://172.16.1.197:8097/iConn/iconnHandler.do"

    @staticmethod
    def release():
        """
        Release url
        :return:
        """
        return "http://172.16.1.195:8097/iConn/iconnHandler.do"

    @staticmethod
    def live():
        """
        Live url
        :return:
        """
        return "http://172.16.1.81:8088/iConn/iconnHandler.do"

if __name__ == '__main__':
    url = Path()
    print(url.dev())
    print(url.release())
    print(url.live())