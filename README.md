# Message Acknowledgments and Remote Procedure Call in RabbitMQ

Source code from RabbitMQ tech talk.


### Prerequisites

To run project you need Python 3.6 version or above to be installed on your computer.

To install project requirements, simply use: 

```
pip install -U -r requirements.txt 
```

## Sources

* [RabbitMQ](https://www.rabbitmq.com/confirms.html) - Consumer Acknowledgements and Publisher Confirms 
* [RabbitMQ](https://www.rabbitmq.com/nack.html) - Negative Acknowledgments
* [RabbitMQ](http://www.rabbitmq.com/blog/2011/02/10/introducing-publisher-confirms/) - Publisher Confirms
* [RabbitMQ](https://www.rabbitmq.com/persistence-conf.html) - Persistence Configuration
* [RabbitMQ](https://www.rabbitmq.com/reliability.html) - Reliability Guide
* [pika.readthedocs.io](http://pika.readthedocs.io/en/latest/examples/blocking_basic_get.html) - Using the Blocking Connection to get a message from RabbitMQ
* [pika.readthedocs.io](http://pika.readthedocs.io/en/0.10.0/modules/channel.html) - Channel documentation
* [jack-vanlightly.com](https://jack-vanlightly.com/blog/2017/3/10/rabbitmq-the-different-failures-on-basicpublish) - Types of Publishing Failures - RabbitMq Publishing Part 1
* [jack-vanlightly.com](https://jack-vanlightly.com/blog/2017/3/11/sending-messages-in-bulk-and-tracking-delivery-status-rabbitmq-publishing-part-2) - Sending Messages in Bulk and Tracking Delivery Status - RabbitMq Publishing Part 2
* [jack-vanlightly.com](https://jack-vanlightly.com/blog/2017/3/12/how-to-deal-with-unroutable-messages-rabbitmq-publishing-part-3) - How to Deal with Unroutable Messages - RabbitMq Publishing Part 3
* [Medium](https://medium.com/ibm-watson-data-lab/handling-failure-successfully-in-rabbitmq-22ffa982b60f) - Handling Failure Successfully in RabbitMQ
* [Github](https://github.com/LeanKit-Labs/wascally/issues/84) - Differences between acknowledgments 1
* [Github](https://github.com/eandersson/python-rabbitmq-examples/blob/master/Flask-examples/amqpstorm_threaded_rpc_client.py) - Flask and asynchronous RPC using pika
* [Stackoverflow](https://stackoverflow.com/questions/28794123/ack-or-nack-in-rabbitmq) - Differences between acknowledgments 2
* [Stackoverflow](https://stackoverflow.com/questions/6386117/rabbitmq-use-of-immediate-and-mandatory-bits) - Immidiate and mandatory messages
* [Stackoverflow](https://stackoverflow.com/questions/42813355/does-pika-confirm-delivery-mean-confirm-when-broker-got-the-message-or-when-cons) - Confirm delivery explained

## Practice
Make your own example of remote procedure call. Think about following problems and try to solve them:
1. How should the client react if there are no servers running?
2. Should a client have some kind of timeout for the RPC?
3. If the server malfunctions and raises an exception, should it be forwarded to the client?
4. Protecting against invalid incoming messages (e.g. checking bounds) before processing.
