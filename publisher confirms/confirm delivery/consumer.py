import pika

case = 'publisher_confirms'

#  Connection open
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#  Exchange
channel.exchange_declare(exchange=case,
                         exchange_type='direct')

#  Queue
queue = channel.queue_declare(queue=case)


#  Binding
channel.queue_bind(queue=case,
                   exchange=case,
                   routing_key=case)


#  Callback
def callback(ch, method, properties, body):
    print(body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


#  Consume
channel.basic_consume(callback,
                      queue=case,
                      no_ack=False)
channel.start_consuming()
