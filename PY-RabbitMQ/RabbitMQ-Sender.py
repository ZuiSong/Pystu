import json
import logging
from datetime import date, datetime
from time import sleep, time

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.10.202'))
channel = connection.channel()
print(datetime.now())
for i in range(10):
    print(i)
    s = json.dumps({'msg{}'.format(i): "123"})
    channel.basic_publish(exchange="amq.topic", routing_key="HOMEPAGE_66666", body=s)

print(datetime.now())

channel.close()
connection.close()
