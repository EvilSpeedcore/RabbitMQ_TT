import json
import pika
import uuid


class LocalNewsRpcClient(object):

    def __init__(self):

        #  Connection open
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()

        #  Callback queue
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        #  Consume
        self.channel.basic_consume(self.on_response,
                                   no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        """Client action on message receive."""
        if self.corr_id == props.correlation_id:
            self.response = json.loads(body)
            for index, each in enumerate(self.response, start=1):
                print(f'{index}. {each}')

    def request(self):
        """Make news articles request to server."""
        self.response = None

        #  Generate unique ID to catch appropriate response
        self.corr_id = str(uuid.uuid4())

        #  Tell server that you want to see news articles publishing a message
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,
                                   ),
                                   body='')

        #  Wait for appropriate response arrival
        while self.response is None:
            self.connection.process_data_events()


local_news = LocalNewsRpcClient()
local_news.request()
