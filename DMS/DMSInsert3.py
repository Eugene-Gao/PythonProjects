#！coding=utf-8
from pykafka import KafkaClient

import json

# from sqlOperators import *
import logging
import time
import sys
import random
import string
client = KafkaClient(hosts='192.168.43.10:9092')

topic = client.topics['operation_3rd1']

producer = topic.get_producer()
pk=[]
producer.start()
count=0
for i in range(70):
    dm_value=random.randint(500,700)
    mc_value=''.join(random.sample(string.ascii_letters,12))
    if dm_value not in pk:
        time_stamp=int(time.time())
        count+=1;
        pk.append(dm_value)
        msg_dict={
        "operationSource":"XX_PLATFORM",
        "data":[{
        "operationType":"INSERT",
        "objectCode":"dm",
        "objectCodeValue":"%d"%dm_value,
        "schema":"xiaoka_kudu",
        "table":"nz_dic_bmfs",
        "columns":[{"name":"dm","value":"%d"%dm_value},{"name":"mc","value":"%s"%mc_value},{"name":"slsj","value":"%d"%time_stamp}]
        }]
        }
        msg=json.dumps(msg_dict)
        print msg
        producer.produce(msg)
        time.sleep(1)
producer.stop()

print "插入条数为：%d"%count
