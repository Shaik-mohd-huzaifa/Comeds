#!/usr/bin/env python

from confluent_kafka import Consumer


def TopicConsumer(topic):

    config = {
        # User-specific properties that you must set
        "bootstrap.servers": "<Your_Bootstrap_Servers>",  # e.g., 'pkc-p11xm.us-east-1.aws.confluent.cloud:9092'
        "sasl.username": "<Your_SASL_Username>",  # e.g., 'AJBGJNJ6QJLHAEWW'
        "sasl.password": "<Your_SASL_Password>",  # e.g., 'iaf1XTmD5UYPVuWX6SdCfFRgrI9FuXhExTpIwuiG4UxuYfdm7FrpBgHpLcjHtJfl'
        # Fixed properties
        "security.protocol": "SASL_SSL",
        "sasl.mechanisms": "PLAIN",
        "acks": "all",
    }

    # Create Consumer instance
    consumer = Consumer(config)

    # Subscribe to topic
    topic = "icu_availability_status"
    consumer.subscribe([topic])

    # Poll for new messages from Kafka and print them.
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                # Initial message consumption may take up to
                # `session.timeout.ms` for the consumer group to
                # rebalance and start consuming
                print("Waiting...")
            elif msg.error():
                print("ERROR: %s".format(msg.error()))
            else:
                # Extract the (optional) key and value, and print.
                print("Consumed event from topic {topic}: key = {key:12} value = {value:12}".format(
                    topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
    except KeyboardInterrupt:
        pass
    finally:
        # Leave group and commit final offsets
        consumer.close()
