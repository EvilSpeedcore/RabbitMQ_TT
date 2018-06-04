import pika

case = 'reject_without_requeue'

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
    ch.basic_reject(delivery_tag=method.delivery_tag, requeue=False)


#  Consume
channel.basic_consume(callback,
                      queue=case,
                      no_ack=False)
channel.start_consuming()
