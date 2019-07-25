from pykafka import KafkaClient
from pykafka.common import OffsetType
host = '192.168.0.202'
client = KafkaClient(hosts="%s:9092"% host)

print client.topics


topic = client.topics['kafkaTest']
# consumer = topic.get_balance(consumer_group='test', consumer_id='test1',reset_offset_on_start=True)

consumer = topic.get_simple_consumer(auto_offset_reset=OffsetType.LATEST,reset_offset_on_start=True,fetch_message_max_bytes=2048576000, num_consumer_fetchers=10)

# while True:
#     x=consumer.consume()
#     if x is not None:
#         print x

for message in consumer:
    if message is not None:
        print message.offset, message.value


