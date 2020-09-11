#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys
import datetime
import socket, sys
import paho.mqtt.client as mqtt


# pip3 install paho-mqtt

# 服务器地址
strBroker = "192.168.200.64"
# 通信端口
port = 1883
# 用户名
username = ''
# 密码
password = ''
# 订阅主题名
topic = 'Edgex-test1'


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
    mqttMsg = json.loads(msgPayload.decode('utf-8'))
    #TODO: serializing to a file

    #TODO: send the msg to LORA

    print ("Exec:", mqttMsg)



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

    mqttc.connect(strBroker, port, 60)
    mqttc.subscribe(topic, 0)
    # mqttc.loop_start()   # 以start方式运行，需要启动一个守护线程，让服务端运行，否则会随主线程死亡
    mqttc.loop_forever()