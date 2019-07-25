# -*- coding: utf-8 -*-

"""
"""
from pykafka import KafkaClient
from pykafka.common import OffsetType
from com.caeit.jn2xx.config.configParam import ConfigParameters
from com.caeit.jn2xx.utils.datatypeUtil import str2Utf8Byte

kafkaCfg = ConfigParameters().kafkaConfig_local
# kafkaCfg = ConfigParameters().kafkaConfig_192_168_43_30
# kafka 客户端创建
kafkaClient = KafkaClient(hosts=kafkaCfg["host"])
getterTopic = kafkaClient.topics[str2Utf8Byte(kafkaCfg["getterTopic"])]
# 获得最新的 consumer offset
lastOffset = getterTopic.latest_available_offsets()
kafkaGetter = getterTopic.get_simple_consumer( \
    consumer_group=str2Utf8Byte(kafkaCfg["getterTopic"]), \
    auto_offset_reset=OffsetType.LATEST, \
    reset_offset_on_start=True)

while True:
    getterMsg = kafkaGetter.consume()
    if getterMsg is None:
        continue
    else:
        print("kafkaGetter:getterMsg: ", getterMsg.value)
