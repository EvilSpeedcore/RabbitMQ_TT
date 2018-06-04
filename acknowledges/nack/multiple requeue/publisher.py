import faker
import pika

case = 'nack_multiple_requeue'

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


#  Publish
for _ in range(1, 4):
    channel.basic_publish(exchange=case,
                          routing_key=case,
                          body=get_name())

#  Connection close
connection.close()
