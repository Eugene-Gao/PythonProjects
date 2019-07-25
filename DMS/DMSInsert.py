# ！coding=utf-8
from pykafka import KafkaClient

import json

# from sqlOperators import *
import logging
import time
import sys
import random
import string

client = KafkaClient(hosts='bigdata6:9092')

topic = client.topics['operation']

producer = topic.get_producer()
pk = []
producer.start()
count = 0
for i in range(1):
    dm_value = random.randint(100, 200)
    mc_value = ''.join(random.sample(string.ascii_letters, 12))
    if dm_value not in pk:
        time_stamp = int(time.time())
        count += 1;
        pk.append(dm_value)
        msg_dict = {
    "data": [
        {
            "schema": "demo_kudu",
            "objectCodeValue": "dn-03051543",
            "objectCode": "dxbm",
            "columns": [
                {
                    "name": "sblb",
                    "value": "3"
                },
                {
                    "name": "dxfl",
                    "value": "1"
                },
                {
                    "name": "dxmc",
                    "value": "dn-03051543"
                },
                {
                    "name": "dxbm",
                    "value": "dn-03051543"
                }
            ],
            "operationType": "INSERT",
            "table": "xx_sb_jbsx"
        },
        {
            "schema": "demo_kudu",
            "objectCodeValue": "dn-03051543",
            "objectCode": "dxbm",
            "columns": [
                {
                    "name": "kzmc",
                    "value": "dn-03051543"
                },
                {
                    "name": "dxbm",
                    "value": "dn-03051543"
                }
            ],
            "operationType": "INSERT",
            "table": "xx_sb_kzsx_dn"
        }
    ],
    "operationSource": "XX_PLATFORM"
}
        msg = json.dumps(msg_dict)
        print msg
        producer.produce(msg)
        time.sleep(1)
producer.stop()

print "插入条数为：%d" % count
