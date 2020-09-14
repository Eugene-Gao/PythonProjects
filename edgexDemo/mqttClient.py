#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import json
from tkinter import messagebox

import paho.mqtt.client as mqtt

# pip3 install paho-mqtt

# 服务器地址
from communications.socketClient import runSocketClinet
from config.configParam import ConfigParameters
from dataCompress.gzipBase64Compress import gzip_zip
from utils.fileManager import wrfile


# strBroker = "192.168.200.64"
# # 通信端口
# port = 1883
# # 用户名
# username = ''
# # 密码
# password = ''
# # 订阅主题名
# topic = 'Edgex-test1'


# ======================================================
def on_connect(mqttc, obj, rc):
    print("OnConnetc, rc: " + str(rc))


def on_publish(mqttc, obj, mid):
    print("OnPublish, mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    # print("Log:" + string)
    pass


def on_message(mqttc, obj, msg):
    curtime = datetime.datetime.now()
    strcurtime = curtime.strftime("%Y-%m-%d %H:%M:%S")
    # print(strcurtime + ": " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    on_exec(msg.payload)


def on_exec(msgPayload):
    # get the message from edgeX of the edge side
    # msgPayload bytes are transferred to a string
    msgPayload_str = msgPayload.decode('utf-8')
    # serialize to a file
    # wt_file_name = "C:/pythonFiles/randomValue-1.json"
    # appending a file
    # wrpuls_file_rlt = wrfile(wt_file_name).wrpuls_file(msgPayload_str)
    # 增加报警标识符
    wrap_mqttMsg_str = wrap_mqttMsg(msgPayload_str)
    # print("发送云端数据: ", wrap_mqttMsg_str)
    # 向物联设备发送指令
    socketConfig_edgeSide = ConfigParameters().socketConfig_edgeSide
    rtnEdgeSideMsg = runSocketClinet(socketConfig_edgeSide["host"], socketConfig_edgeSide["port"],
                                     socketConfig_edgeSide["msgsize"], wrap_mqttMsg_str)

    # if len(rtnEdgeSideMsg) != 0 and rtnEdgeSideMsg.isspace() is False:
    #     print("rtnEdgeSideMsg: ", rtnEdgeSideMsg)
    # gzip+base64压缩
    wrap_mqttMsgZip_str = str(gzip_zip(wrap_mqttMsg_str))
    print("发送云端加密压缩数据: ", wrap_mqttMsgZip_str)
    # 向云端发送采集数据
    socketConfig_local = ConfigParameters().socketConfig_local
    rtnCloudSideMsg = runSocketClinet(socketConfig_local["host"], socketConfig_local["port"],
                                      socketConfig_local["msgsize"],
                                      wrap_mqttMsg_str)

    if rtnCloudSideMsg == "0":
        # 返回值=0，误报
        returnDict = json.loads(wrap_mqttMsg_str)
        print(returnDict)
        returnDict["alterFlag"] = "2000"
        runSocketClinet(socketConfig_edgeSide["host"], socketConfig_edgeSide["port"],
                        socketConfig_edgeSide["msgsize"], json.dumps(returnDict))
        # messagebox.showinfo("反馈执行操作", "检测异常，关闭警报")
    elif rtnCloudSideMsg == "1":
        # launch the air-condition
        messagebox.showinfo("反馈执行操作", "启动制冷装置")

    print("rtnCloudSideMsg: ", rtnCloudSideMsg)


def wrap_mqttMsg(mqttMsg):
    """
    adding the mqtt msg with alert flag, then send it to Edgex on the cloud side
    :param mqttMsg:
    :return: wrapmsg
    """

    if len(mqttMsg) == 0 and mqttMsg.isspace():
        # 字符串为null，直接返回
        wrapMsg = ""
    else:
        # 转化为dict
        mqttDict = json.loads(mqttMsg)
        # 获取 reading的value
        readingsDict = mqttDict.get('readings')[0]
        # print(readingsDict["value"])
        if float(readingsDict["value"]) > ConfigParameters.thresholdValue_enums["tempUpThreshold"]:
            # The temp exceeds the tempUpThreshold, set the alter value
            wrapDict = dict(mqttDict, **{"alterFlag": "1001"})
        elif float(readingsDict["value"]) < ConfigParameters.thresholdValue_enums["tempLowThreshold"]:
            # The temp belows the tempLowThreshold, set the alter value
            wrapDict = dict(mqttDict, **{"alterFlag": "1002"})
        else:
            # The normal temp
            wrapDict = dict(mqttDict, **{"alterFlag": "1000"})
        # 转化为str
        wrapMsg = json.dumps(wrapDict)
    # return value
    return wrapMsg


# =====================================================
if __name__ == '__main__':
    mqttc = mqtt.Client("MqttClientTest")
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe
    mqttc.on_log = on_log

    # 设置账号密码（如果需要的话）
    # mqttc.username_pw_set(username, password=password)
    #########################################################################
    # 配置 mqtt 参数
    # mqttconfig_dict = ConfigParameters().mqttConfig_192_168_200_64
    mqttconfig_dict = ConfigParameters().mqttConfig_192_168_1_108
    #########################################################################
    mqttc.connect(mqttconfig_dict["strBroker"], mqttconfig_dict["port"], 60)
    mqttc.subscribe(mqttconfig_dict["topic"], 0)
    # mqttc.loop_start()   # 以start方式运行，需要启动一个守护线程，让服务端运行，否则会随主线程死亡
    mqttc.loop_forever()
