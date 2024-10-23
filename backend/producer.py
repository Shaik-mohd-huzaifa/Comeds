#!/usr/bin/env python

from random import choice
from confluent_kafka import Producer
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':

    config = {
        # User-specific properties that you must set
        'bootstrap.servers': 'pkc-p11xm.us-east-1.aws.confluent.cloud:9092',
        'sasl.username':     'AJBGJNJ6QJLHAEWW',
        'sasl.password':     'iaf1XTmD5UYPVuWX6SdCfFRgrI9FuXhExTpIwuiG4UxuYfdm7FrpBgHpLcjHtJfl',

        # Fixed properties
        'security.protocol': 'SASL_SSL',
        'sasl.mechanisms':   'PLAIN',
        'acks':              'all'
    }

    # Create Producer instance
    producer = Producer(config)

    # Optional per-message delivery callback (triggered by poll() or flush())
    # when a message has been successfully delivered or permanently
    # failed delivery (after retries).
    def delivery_callback(err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))
        else:
            print("Produced event to topic {topic}: key = {key:12} value = {value:12}".format(
                topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))

    # Produce data by selecting random values from these lists.
    topic = "patient_reportss"
    user_ids = ['eabara', 'jsmith', 'sgarcia', 'jbernard', 'htanaka', 'awalther']
    products = ['book', 'alarm clock', 't-shirts', 'gift card', 'batteries']

    count = 0
    for _ in range(10):
        user_id = choice(user_ids)
        product = choice(products)
        producer.produce(topic, product, user_id, callback=delivery_callback)
        count += 1

    # Block until the messages are sent.
    producer.poll(10000)
    producer.flush()