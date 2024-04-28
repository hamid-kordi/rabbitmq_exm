import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()

ch.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

result = ch.queue_declare(queue='', exclusive=True)
qname = result.method.queue

ch.queue_bind(exchange='direct_logs',
                   queue=qname,
                   routing_key='error')

print('wait for messages')

def callback(ch,method,properties,body):
    with open('errpr_log.log','a') as f : 
        f.write(str(f'{body}') + '\n')
    

ch.basic_consume(queue=qname,on_message_callback=callback,auto_ack=True)
ch.start_consuming()