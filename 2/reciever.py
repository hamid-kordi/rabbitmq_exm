import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

ch2 = connection.channel()

ch2.queue_declare(queue="first", durable=True)
print("wait for massegess")


def callback(ch, method, propertice, body):
    print(f"received messages {body}")
    time.sleep(9)
    print("done")
    print(propertice.headers)
    print(method)
    ch.basic_ack(delivery_tag=method.delivery_tag)
# https://www.rabbitmq.com/docs/publishers
# down table == propertices 
# up table == method

ch2.basic_qos(prefetch_count=1)

ch2.basic_consume(queue="first", on_message_callback=callback,auto_ack=False)

ch2.start_consuming()
