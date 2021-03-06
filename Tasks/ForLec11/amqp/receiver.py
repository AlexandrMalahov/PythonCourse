# файл receive.py

import pika
import time
import random

connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='hello', durable=True)

def callback(ch, method, properties, body):
    print('Start processing {}'.format(body.decode()))
    t = time.time()
    time.sleep(random.randint(1, 5))
    print('Processed for {:3.2f} sec.'.format(time.time() - t))
    channel.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=False)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()