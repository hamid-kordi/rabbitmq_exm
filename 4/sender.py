import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()

ch.exchange_declare(exchange='direct_logs',exchange_type='direct')

mess = {
    "info" : "this is info",
    "error" : "this is an error",
    "warning" : "rhis is warning"

}


for k,v in mess.items():
    ch.basic_publish(exchange='direct_logs',routing_key=k,body=v)


connection.close()
