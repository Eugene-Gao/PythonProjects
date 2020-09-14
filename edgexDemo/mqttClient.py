#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import json

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
    print("Log:" + string)


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
    wt_file_name = "C:/pythonFiles/randomValue-1.json"
    # appending a file
    wrpuls_file_rlt = wrfile(wt_file_name).wrpuls_file(msgPayload_str)
    # add the alert flag
    wrap_mqttMsg_str = wrap_mqttMsg(msgPayload_str)
    print("Exec:", wrap_mqttMsg_str)
    socketConfig_edgeSide = ConfigParameters().socketConfig_edgeSide
    rtnEdgeSideMsg = runSocketClinet(socketConfig_edgeSide["host"], socketConfig_edgeSide["port"], socketConfig_edgeSide["msgsize"],
                             wrap_mqttMsg_str)

    if len(rtnEdgeSideMsg) == 0 and rtnEdgeSideMsg.isspace():
        print(rtnEdgeSideMsg)
    # gzip+base64压缩
    wrap_mqttMsg_str = str(gzip_zip(wrap_mqttMsg_str))
    # TODO: send the msg to LORA
    # 创建一个客户端的socket对象
    socketConfig_local = ConfigParameters().socketConfig_local
    rtnCloudSideMsg = runSocketClinet(socketConfig_local["host"], socketConfig_local["port"], socketConfig_local["msgsize"],
                             wrap_mqttMsg_str)
    print(rtnCloudSideMsg)


def wrap_mqttMsg(mqttMsg):
    """
    adding the mqtt msg with alert flag, then send it to Edgex on the cloud side
    :param mqttMsg:
    :return: wrapmsg
    """

    if len(mqttMsg) == 0 and mqttMsg.isspace():
        wrapMsg = ""
    else:
        # get reading
        mqttDict = json.loads(mqttMsg)
        readingsDict = mqttDict.get('readings', '')[0]
        print(readingsDict["value"])
        if float(readingsDict["value"]) >= ConfigParameters.thresholdValue_enums["tempThreshold"]:
            # The temp exceeds the threshold, set the alter value
            wrapDict = dict(mqttDict, **{"alterFlag" : "1001"})
        else:
            wrapDict = dict(mqttDict, **{"alterFlag": "1000"})
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
