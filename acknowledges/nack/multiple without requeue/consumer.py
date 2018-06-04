import pika

case = 'nack_multiple_without_requeue'

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


#  Get 3 messages from queue
responses = [channel.basic_get(case) for _ in range(1, 4)]
*_, last_response = responses
method = last_response[0]

#  Acknowledge only last one with it's delivery tag
channel.basic_nack(delivery_tag=method.delivery_tag,
                   multiple=True,
                   requeue=False)
