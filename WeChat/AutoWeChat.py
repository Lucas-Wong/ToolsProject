#! /usr/bin/env python
#_*_coding:utf-8_*_

import itchat, time
from itchat.content import *

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    #itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])
    itchat.send_msg('已经收到了消息，消息内容为%s' % msg['Text'], toUserName=msg['FromUserName'])
    return "T reveived: %s" % msg["Text"]  # 返回的给对方的消息，msg["Text"]表示消息的内容

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg['Text'](msg['FileName'])
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['isAt']:
        #itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])
        itchat.send_msg("我已经收到了来自{0}的消息，实际内容为{1}".format(msg['ActualNickName'], msg['Text']),
                        toUserName=msg['FromUserName'])

itchat.auto_login(True, hotReload=True)
itchat.run(True)