import faker
import pika

case = 'reject_without_requeue'

#  Connection open
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#  Exchange declare
channel.exchange_declare(exchange=case,
                         exchange_type='direct')


#  Messages
def get_name():
    message = f'Hello, {faker.Faker().name()}!'
    return message


#  Publish
channel.basic_publish(exchange=case,
                      routing_key=case,
                      body=get_name())

#  Connection close
connection.close()