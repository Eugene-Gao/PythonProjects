from pykafka import KafkaClient

host = '192.168.43.80'
# !/bin/env python
from kafka import KafkaConsumer

# connect to Kafka server and pass the topic we want to consume
consumer = KafkaConsumer('sub7', group_id='test_group',
                         bootstrap_servers=['192.168.43.80'])
try:
    for msg in consumer:
        print(msg)
        print("%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value))
except KeyboardInterrupt, e:
    print(e)

