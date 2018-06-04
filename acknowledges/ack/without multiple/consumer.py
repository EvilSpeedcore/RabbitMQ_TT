import pika

case = 'ack_without_multiple'

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

#  Get 3 messages
responses = [channel.basic_get(case) for _ in range(1, 4)]

#  Acknowledge only last message with it's delivery tag
#  First two messages will remain in queue
*_, last_response = responses
method = last_response[0]
channel.basic_ack(delivery_tag=method.delivery_tag)
