#!/usr/bin/env python3

import pika

connection = pika.BlockingConnection(pika.URLParameters("amqp://guest:guest@rabbit:5672"))
channel = connection.channel()
channel.queue_declare(queue='4messages')

print('[*] Write your messages. To exit press CTRL+C.')
try:
	while True:
		data = input('[*] Enter your message: ')
		channel.basic_publish(exchange='',routing_key='4messages', body=data)
		print('[*] Message sent')

except KeyboardInterrupt:
    exit()
