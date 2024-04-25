import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))


ch1 = connection.channel()


ch1.exchange_declare(exchange="logs", exchange_type="fanout")
ch1.basic_publish(exchange="logs",routing_key='', body='this is the test for fan out')

print("sent messages")

connection.close()