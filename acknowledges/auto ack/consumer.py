import time
import pika

case = 'auto_ack'

#  Connection open
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#  Exchange
channel.exchange_declare(exchange=case,
                         exchange_type='direct')
#  Queue
queue = channel.queue_declare(queue=case)

#  Binding
channel.queue_bind(exchange=case,
                   queue=case,
                   routing_key=case)


#  Callback
def callback(ch, method, properties, body):
    time.sleep(10)
    with open('random', 'wb') as f:
        f.write(body)


#  Consume
channel.basic_consume(callback,
                      queue=case,
                      no_ack=True)
channel.start_consuming()
