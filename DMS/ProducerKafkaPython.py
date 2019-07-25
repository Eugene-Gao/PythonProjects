# -*- coding: utf-8 -*-
import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='192.168.0.203:9092'\
                         ,max_request_size=209715200,buffer_memory=209715200)

with open("C:\Users\hshi\Desktop\insert-sql.txt","r") as f:
    msg=f.read()
print msg
# msg='hello,world'
producer.send('kafkaTest5',msg,partition=0)
producer.close()


