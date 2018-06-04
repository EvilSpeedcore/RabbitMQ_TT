import os
import subprocess
import time
import faker
import pika


case = 'publisher_confirms_resend'

#  Connection open
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#  Confirm
channel.confirm_delivery()


#  Exchange
channel.exchange_declare(exchange=case,
                         exchange_type='direct')

message = faker.Faker().text()


def send_message():
    response = channel.basic_publish(exchange=case,
                                     body=message,
                                     routing_key=case,
                                     mandatory=True)
    return response


consumer_running = send_message()
if consumer_running:
    print('Consumer was up. Message was sent.')
    connection.close()
else:
    print('Cannot route message to queue. Starting consumer...')
    path = os.getcwd() + '\consumer.py'
    #  Start consumer and resent message
    process = subprocess.Popen(['python', path])
    time.sleep(5)
    send_message()
    connection.close()
