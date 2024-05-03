import pika

import uuid

class Sender:
    def __init__(self) -> None:
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.ch = self.connection.channel()
        result = self.ch.queue_declare(queue='',exclusive=True)
        self.queuename = result.method.queue


    def call(self,n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.ch.basic_publish(exchange='',routing_key='rpc_queue',
                              properties=pika.BasicProperties(reply_to=self.queuename,correlation_id=self.corr_id),body=str(n))

        pass



send = Sender()

send.call(30)