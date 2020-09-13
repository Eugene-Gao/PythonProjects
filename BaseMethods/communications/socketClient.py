#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'Eugene Gao'
__date__ = '20200913'

import socket

def socketClient(client, host, port, msgsize, sendmsg):
    '''

    :param client:
    :param host:
    :param port:
    :param sendmsg:
    :return:
    '''
    # 连接服务端
    client.connect((host, port))
    # 发送数据，以二进制的形式发送数据，所以需要进行编码
    client.send(sendmsg.encode("utf-8"))
    msg = client.recv(msgsize)
    # 关闭客户端
    client.close()
    # 接收服务端返回的数据，需要解码
    return msg.decode("utf-8")

if __name__ == '__main__':
    socketConfig_local = {
        # 设置服务端的ip地址
        "host" : "127.0.0.1",
        # 设置端口
        "port" : 9999,
        "msgsize": 2048
    }
    sendmsg = "连接服务端"
    # 创建一个客户端的socket对象
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    rtnMsg = socketClient(client, socketConfig_local["host"], socketConfig_local["port"], socketConfig_local["msgsize"], sendmsg)
    print(rtnMsg)