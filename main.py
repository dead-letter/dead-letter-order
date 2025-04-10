import os
import sys
import pika
import time
from pika import credentials

# reference
# https://www.rabbitmq.com/tutorials/tutorial-one-python#using-the-pika-python-client


def order_received(channel, method, properties, body):
    pass


def main():
    # dead-letter-data.dead-letter.svc.cluster.local
    db_service = os.environ["DB_SERVICE_URL"]
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        os.environ["MQ_URL"], credentials=credentials.PlainCredentials(os.environ["MQ_USER"], os.environ["MQ_PASS"])))
    channel = connection.channel()

    channel.queue_declare(queue=os.environ["MQ_QUEUE"])

    channel.basic_consume(
        queue=os.environ["MQ_QUEUE"],
        auto_ack=True,
        on_message_callback=order_received,
    )

    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
