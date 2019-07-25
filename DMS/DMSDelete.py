#！coding=utf-8
from pykafka import KafkaClient

import json

# from sqlOperators import *
import logging
import time
import sys

client = KafkaClient(hosts='192.168.1.30:9092')

topic = client.topics['operation_3rd1']

producer = topic.get_producer()

producer.start()

msg_dict={
    "operationSource":"XX_PLATFORM",
    "data":[{
    "operationType":"DELETE",
    "objectCode":"dm",
    "objectCodeValue":"500",
    "schema":"xiaoka_kudu",
    "table":"nz_dic_bmfs",
    "columns":[{"name":"dm","value":"500",},\
               ]
}]
}
msg=json.dumps(msg_dict)
print msg

producer.produce(msg)

producer.stop()