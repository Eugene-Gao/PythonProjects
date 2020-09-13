#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'Eugene Gao'
__date__ = '20200913'

import socket

def socketServer(socketserver, host, port, msgsize, sendmsg):
    # 绑定地址（包括ip地址会端口号）
    socketserver.bind((host, port))
    # 设置监听
    socketserver.listen(5)
    # 等待客户端的连接
    # 注意：accept()函数会返回一个元组
    # 元素1为客户端的socket对象，元素2为客户端的地址(ip地址，端口号)
    clientsocket, addr = socketserver.accept()

    # while循环是为了能让对话一直进行，直到客户端输入q
    while True:

        # 接收客户端的请求
        recvmsg = clientsocket.recv(msgsize)

        # 把接收到的数据进行解码
        strData = recvmsg.decode("utf-8")
        # 判断客户端是否发送Quit，是就退出此次对话
        if strData == 'Quit':
            break
        # ToDo: logical service
        print("收到:" + strData)
        # 对要发送的数据进行编码
        clientsocket.send(sendmsg.encode("utf-8"))

    socketserver.close()

if __name__ == '__main__':
    socketConfig_local = {
        # 设置服务端的ip地址
        "host" : "127.0.0.1",
        # 设置端口
        "port" : 9999,
        "msgsize": 2048
    }
    # 创建服务端的socket对象socketserver
    socketserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketServer(socketserver, socketConfig_local["host"], socketConfig_local["port"], socketConfig_local["msgsize"], "Success!")

