# -*- coding: utf-8 -*-
__author__ = 'Eugene Gao'
__date__ = '2018.08.17'

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

    dbconfig_local_nz_wltsfx = {
        "host": "192.168.162.10",
        "port": 3306,
        "user": "root",
        "password": "123456",
        "dataBase": "nz_wltsfx",
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

    # Dev DB
    dbconfig_192_168_43_10_nz_wltsfx = {
        "host": "192.168.43.10",
        "port": 3306,
        "user": "root",
        "password": "root",
        "dataBase": "nz_wltsfx",
        "charset": "utf8"
    }

    # Dev kafka
    kafkaConfig_192_168_43_30 = {
        "host":"192.168.43.30:9092",
        "senderTopic": "test2",
        "consumerTopic": "test2",
        "producerTopic":"test3",
        "getterTopic": "test3"
    }

