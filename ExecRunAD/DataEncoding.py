# _*_ coding:utf-8 _*_
"""
-----------------------------------------------------------
 Name：            ToolsProject/DataEncoding
 Purpose：         

 Author：          lucas.wang

 Created：         2018-07-30
 Copyright：       (C) lucas.wang 2018
 Licence:          MIT
 ----------------------------------------------------------
"""
# ! /usr/bin/env python

import base64
from pyDes import *
import six

class DataEncoding(object):
    """
    DES encoding function
    """
    # Key
    Des_Key = "BOC_PLFP".encode()
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
        encode_string = base64.encodebytes(bytes_string)
        # print(encode_str)
        return encode_string

    def b64_decoding(self):
        """
        Base64
        :return:
        """
        bytes_string = self.String
        # print(bytes_string)

        decode_string = base64.decodebytes(bytes_string)
        # print(decode_string)
        return decode_string

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
    run_encode = DataEncoding("Copyright (c) 2012 Doucube Inc. All rights reserved.")
    encode_str = run_encode.b64_encoding()
    print(encode_str)
    run_decode = DataEncoding(encode_str)
    decode_str = run_decode.b64_decoding()
    print(decode_str)
