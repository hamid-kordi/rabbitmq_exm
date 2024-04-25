import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
ch = connection.channel()

ch.exchange_declare(exchange="logs", exchange_type="fanout")

result = ch.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue
ch.queue_bind(exchange="logs", queue=queue_name)
print("wait for mesages")


def callback(ch, method, propertice, body):
    print("recieved messages")


ch.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
ch.start_consuming()
