import pika

connction = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))


ch1 = connction.channel()

ch1.queue_declare(queue="first", durable=True)
messages = "hello this is one test messages"

ch1.basic_publish(
    exchange="",
    routing_key="first",
    body=messages,
    properties=pika.BasicProperties(delivery_mode=2, headers={"amir": "aslan"}),
)
print("messages sent")


connction.close()
