#！coding=utf-8
from pykafka import KafkaClient

import json

# from sqlOperators import *
import logging
import time
import sys
import random
import string
client = KafkaClient(hosts='192.168.0.202:9092')

topic = client.topics['kafkaTest4']

with open("C:\Users\hshi\Desktop\insert-sql.txt","r") as f:
    msg=f.read()
print type(msg)
# msg='hello'


producer = topic.get_producer(max_request_size=209715200)
producer.start()

producer.produce(msg)
producer.stop()

