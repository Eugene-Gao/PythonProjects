# -*- coding: utf-8 -*-
"""
模拟其他子系统生成 kafka 消息
"""
import json

from pykafka import KafkaClient
from com.caeit.jn2xx.config.configParam import ConfigParameters
from com.caeit.jn2xx.utils.datatypeUtil import str2Utf8Byte
from com.caeit.jn2xx.utils.fileUtil import resolve_json

# Json 文件==========================================================================================================
# 设备
# fileName = "D:/Work/Project/PythonProjects/TestFiles/SourceDir/Insert_sbJbsx.json"
# 链路
# jb_table
fileName = "D:/Work/Project/PythonProjects/TestFiles/SourceDir/Insert_llJbsx.json"
# fileName = "D:/Work/Project/PythonProjects/TestFiles/SourceDir/Update_llJbsx.json"
# fileName = "D:/Work/Project/PythonProjects/TestFiles/SourceDir/Delete_llJbsx.json"
# kz_table
# fileName = "D:/Work/Project/PythonProjects/TestFiles/SourceDir/Insert_llKzsxIdirect.json"
# fileName = "D:/Work/Project/PythonProjects/TestFiles/SourceDir/Update_llKzsxIdirect.json"
# fileName = "D:/Work/Project/PythonProjects/TestFiles/SourceDir/Delete_llKzsxIdirect.json"

# 配置信息==================================================================================================
# kafkaCfg = ConfigParameters().kafkaConfig_local
kafkaCfg = ConfigParameters().kafkaConfig_192_168_43_30

# kafka==================================================================================================
# kafka 客户端创建
kafkaClient = KafkaClient(hosts=kafkaCfg["host"])
senderTopic = kafkaClient.topics[str2Utf8Byte(kafkaCfg["producerTopic"])]
# 获得 producer
kafkaSender = senderTopic.get_producer()
# dict 转换为消息
senderMsg = json.dumps(resolve_json(fileName))
print("kafkaSender:senderMsg: ", senderMsg)
kafkaSender.start()
kafkaSender.produce(str2Utf8Byte(senderMsg))
kafkaSender.stop()