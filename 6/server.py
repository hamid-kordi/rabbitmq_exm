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
    ch.basic_publish(
        exchange="",
        routing_key=proper.reply_to,
        properties=pika.BasicProperties(correlation_id=proper.corolation_id),
        body=str(response),
    )
    ch.basic_ack(delivery_tag = method.delivery())

ch.basic_qos(prefetch_count=1)
ch.basic_consume(queue="", on_message_callback=callback)
print("wait for messages")
ch.start_consuming()
