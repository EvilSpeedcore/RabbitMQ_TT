import faker
import pika

case = 'ack_multiple'

#  Connection open
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#  Exchange
channel.exchange_declare(exchange=case,
                         exchange_type='direct')


#  Message
def get_name():
    message = f'Hello, {faker.Faker().name()}!'
    return message


#  Publish three messages into queue
for _ in range(1, 4):
    channel.basic_publish(exchange=case,
                          routing_key=case,
                          body=get_name())
#  Connection close
connection.close()
