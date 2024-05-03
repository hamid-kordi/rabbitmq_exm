import pika

import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
ch = connection.channel()

ch.queue_declare(queue="rpc_queue")


def callback(ch, method, proper, body):
    n = int(body)
    print("work on masseges")
    time.sleep(3)
    response = n + 1


ch.basic_consume(queue='',on_message_callback=callback)
print('wait for messages')
ch.start_consuming()