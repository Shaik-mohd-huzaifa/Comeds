# Comeds

"Our AI application is a healthcare platform designed for doctors, patients, and administrative staff. It features an intelligent chatbot that automates tasks such as updating doctor availability, scheduling appointments, and providing real-time patient health monitoring from ICU units. The platform also offers dashboards for managing doctor schedules and tracking patient data. This solution benefits healthcare providers by streamlining operations, improving efficiency, and enhancing patient care through quick and accurate information access. 

*Note: The frontend of the application is still under development.*"

Chatbot High level Architecture

![](https://github.com/Shaik-mohd-huzaifa/Comeds/blob/5f06ec6c3372aa2d896560b0b0eb4c8883a2b359/Chatbot%20architecture.png)

Here’s how the configuration should look with placeholders for user-specific properties:

```python
config = {
    # User-specific properties that you must set
    'bootstrap.servers': '<Your_Bootstrap_Servers>', # e.g., 'pkc-p11xm.us-east-1.aws.confluent.cloud:9092'
    'sasl.username':     '<Your_SASL_Username>',     # e.g., 'AJBGJNJ6QJLHAEWW'
    'sasl.password':     '<Your_SASL_Password>',     # e.g., 'iaf1XTmD5UYPVuWX6SdCfFRgrI9FuXhExTpIwuiG4UxuYfdm7FrpBgHpLcjHtJfl'

    # Fixed properties
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms':   'PLAIN',
    'acks':              'all'
}
```
Replace `<Your_Bootstrap_Servers>`, `<Your_SASL_Username>`, and `<Your_SASL_Password>` with your actual configuration values.


Sample .env File
Create a .env file in the project root directory and add the following content:

```env
OPENAI_ENDPOINT = "YOUR_OPENAI_ENDPOINT"
OPENAI_API_KEY = "YOUR_OPEN_AI_KEY"
```

Replace "YOUR_OPENAI_ENDPOINT" and "YOUR_OPEN_AI_KEY" with your actual configuration values.

## Required Connection Configurations for Confluent Kafka

Before running the application, please fill in the following connection configurations for the Confluent Kafka producer, consumer, and admin. These settings are essential for establishing a connection with your Confluent Cloud instance.

```plaintext
# Required connection configs for Confluent Kafka producer, consumer, and admin
bootstrap.servers="SERVER ENDPOINT"          # Replace with your Confluent Kafka server endpoint
security.protocol=SASL_SSL
sasl.mechanisms=PLAIN
sasl.username="API KEY"                      # Replace with your Confluent API key
sasl.password="APIKEY SECRET"                # Replace with your Confluent API key secret

# Best practice for higher availability in librdkafka clients prior to 1.7
session.timeout.ms=45000

client.id="CLOUD_ID"                         # Replace with your Confluent cloud ID
```
Make sure to replace the placeholders with your actual Confluent configuration values before starting the application.
