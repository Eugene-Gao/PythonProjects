# -*- coding: utf-8 -*-
__author__ = 'Eugene Gao'
__date__ = '20200911'

class ConfigParameters(object):
    # 数据库配置信息
    # local DB
    dbconfig_local_test = {
        "host": "192.168.162.10",
        "port": 3306,
        "user": "root",
        "password": "123456",
        "dataBase": "test",
        "charset": "utf8"
    }

    # local kafka
    kafkaConfig_local = {
        "host": "192.168.162.10:9092",
        "senderTopic": "test2",
        "consumerTopic": "test2",
        "producerTopic": "test3",
        "getterTopic": "test3"
    }

    # Dev kafka
    mqttConfig_192_168_200_64 = {
        # mqtt IP address
        "strBroker" : "192.168.200.64",
        # 通信端口
        "port" : 1883,
        # 用户名
        "username" : "",
        # 密码
        "password" : "",
        # 订阅主题名
        "topic" : "Edgex-test1"
    }

