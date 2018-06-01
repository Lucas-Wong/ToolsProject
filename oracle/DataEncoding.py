#! /usr/bin/env python
# _*_coding:utf-8_*_

import base64
from pyDes import *
import six

class DataEncoding(object):
    """
    DES encoding function
    """
    # Key
    Des_Key = "BOC_PLFP".encode(encoding="utf-8")
    # 自定IV向量
    # 0x12, 0x34, 0x56, 0x78, (byte)0x90, (byte)0xab, (byte)0xcd, (byte)0xef
    Des_IV = bytes([0x12, 0x34, 0x56, 0x78, 0x90, 0xab, 0xcd, 0xef])

    def __init__(self, string):
        self.String = string

    def b64_encoding(self):
        """
        Base64
        :return:
        """
        bytes_string = self.String.encode(encoding="utf-8")
        # print(bytesString)
        encode_str = base64.encodebytes(bytes_string)
        # print(encode_str)
        return encode_str

    def b64_decoding(self):
        """
        Base64
        :return:
        """
        bytes_string = self.String
        # print(bytes_string)

        decode_str = base64.decodebytes(bytes_string)
        # print(decode_str)
        return decode_str

    def DesEncrypt(self):
        """
        DES
        :return:
        """
        k = des(self.Des_Key, CBC, self.Des_IV, pad=None, padmode=PAD_PKCS5)
        encrypt_str = k.encrypt(self.String)
        return base64.b64encode(encrypt_str)  # 转base64编码返回
"""
    def DesEncrypt(self):
        k = des(self.Des_Key, CBC, self.Des_IV, pad=None, padmode=PAD_PKCS5)
        print(self.String)
        EncryptStr = k.encrypt(self.String)
        print(EncryptStr)
        return base64.b64encode(EncryptStr)  # 转base64编码返回
"""

if __name__ == '__main__':
    runencode = DataEncoding("Copyright (c) 2012 Doucube Inc. All rights reserved.")
    encodestr = runencode.b64_encoding()
    print(encodestr)
    rundecode = DataEncoding(encodestr)
    decodestr = rundecode.b64_decoding()
    print(decodestr)

