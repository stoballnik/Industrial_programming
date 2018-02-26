#!/usr/bin/env python3

import pika
import pg8000


def callback(ch, method, properties, body):
	print ('[*] The received message: \'{0}\''.format(body.decode()))
	cursor.execute('INSERT INTO tmp (message) VALUES (%s)', (body))
	db_connection.commit()
	print('[x] The message is entered in the database.')


queue_connection = pika.BlockingConnection(pika.URLParameters("amqp://guest:guest@rabbit:5672"))
channel = queue_connection.channel()
channel.queue_declare(queue='4messages')

db_connection = pg8000.connect(user='postgres', password='postgres', host='database')
cursor = db_connection.cursor()

cursor.execute('DROP TABLE IF EXISTS tmp')
cursor.execute('CREATE TABLE IF NOT EXISTS tmp (message VARCHAR(256))')

print('[*] Waiting for messages. To exit press CTRL+C.')
channel.basic_consume(callback,queue='4messages',no_ack=True)

try:
    channel.start_consuming()
except KeyboardInterrupt:
	cursor.execute('SELECT * FROM tmp LIMIT 10')
	results = cursor.fetchall()
	print(results)
	print('[x] This is TOP 10 rows in database.')
	channel.stop_consuming()

db_connection.close()
channel.close()
exit()
