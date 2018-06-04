import faker
import pika

case = 'auto_ack'

#  Connection open
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#  Exchange
channel.exchange_declare(exchange=case,
                         exchange_type='direct')


#  Message
def get_text():
    message = faker.Faker().text()
    return message


#  Publish
channel.basic_publish(exchange=case,
                      routing_key=case,
                      body=get_text())

#  Connection close
connection.close()
