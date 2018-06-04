import faker
import pika

case = 'publisher_confirms'

#  Connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#  Confirm
channel.confirm_delivery()


#  Exchange
channel.exchange_declare(exchange=case,
                         exchange_type='direct')

#  Message
message = f'Hello, {faker.Faker().name()}!'


#  Publish
response = channel.basic_publish(exchange=case,
                                 body=message,
                                 routing_key=case,
                                 mandatory=True)
print(f'Response: {response}')
#  Connection close
connection.close()
