# -*- coding: utf-8 -*-
"""
实现通过 kafka 向其他子系统推送数据库数据变化消息
"""
import pymysql
import json
from pykafka import KafkaClient
from pykafka.common import OffsetType
from com.caeit.jn2xx.utils.datatypeUtil import str2Utf8Byte
from com.caeit.jn2xx.config.configParam import ConfigParameters
from com.caeit.jn2xx.kafkaDbService.service.databaseService import databaseService

# 配置信息==================================================================================================
kafkaCfg = ConfigParameters().kafkaConfig_192_168_43_30
dbConfig_dict = ConfigParameters().dbconfig_192_168_43_10_nz_wltsfx

# 创建数据库连接============================================================================================
dbConnect = pymysql.connect(host=dbConfig_dict["host"], port=dbConfig_dict["port"],
                            user=dbConfig_dict["user"], password=dbConfig_dict["password"],
                            database=dbConfig_dict["dataBase"], charset=dbConfig_dict["charset"])

# kafka====================================================================================================
# kafka 客户端创建
kafkaClient = KafkaClient(hosts=kafkaCfg["host"])
consumerTopic = kafkaClient.topics[str2Utf8Byte(kafkaCfg["consumerTopic"])]
producerTopic = kafkaClient.topics[str2Utf8Byte(kafkaCfg["producerTopic"])]
# 获得最新的 consumer offset
lastOffset = consumerTopic.latest_available_offsets()
kafkaServiceConsumer = consumerTopic.get_simple_consumer( \
    consumer_group=str2Utf8Byte(kafkaCfg["consumerTopic"]), \
    auto_offset_reset=OffsetType.LATEST, \
    reset_offset_on_start=True)
# 获得 producer
kafkaServiceProducer = producerTopic.get_producer()
# 解析 kafka 推送的消息，完成数据库相应操作，并把操作结果推送给订阅的子系统
while True:
    # 获得 kafka 消息
    consumerMsg = kafkaServiceConsumer.consume()
    if consumerMsg is None:
        continue
    else:
        print("kafkaService:consumerMsg offset: ", consumerMsg.offset)
        print("kafkaService:consumerMsg: ", consumerMsg.value)
        # kafka 消息解析为 dict 对象
        msg_dict = json.loads(consumerMsg.value)
        # 调用 databaseService
        view_dict = databaseService(dbConnect, msg_dict)
        # 发送 kafka 消息
        kafkaServiceProducer.start()
        producerMsg = json.dumps(view_dict)
        print("kafkaService:producerMsg: ", producerMsg)
        kafkaServiceProducer.produce(str2Utf8Byte(producerMsg))
        kafkaServiceProducer.stop()

# 关闭数据库连接
dbConnect.close()
