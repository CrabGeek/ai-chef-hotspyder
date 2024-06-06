import pika
from chef_utility.hotspyder_utility import MQ_CHANNEL_CONSUMMING_POOL
from typing import Callable
import server_settings


class RabbitMQClient:

    def __init__(self, address: str) -> None:
        self.__addr = address
        self.__publish_conn: pika.BlockingConnection = None
        self.__consume_conn: pika.BlockingConnection = None

    def init_connections(self):
        try:
            self.__publish_conn = pika.BlockingConnection(
                pika.ConnectionParameters(host=self.__addr)
            )
            self.__consume_conn = pika.BlockingConnection(
                pika.ConnectionParameters(host=self.__addr)
            )

        except Exception as e:
            # TODO: need to log
            print(e)

    def send(
        self,
        channel_name: str,
        payload: str,
        properties: pika.BasicProperties,
        exchange: str = "",
    ):
        with self.__publish_conn.channel() as channel:
            try:
                channel.queue_declare(channel_name)
                channel.basic_publish(
                    exchange=exchange,
                    routing_key=channel_name,
                    body=payload,
                    properties=properties,
                )
            except Exception as e:
                # TODO: need to log
                print(e)

    def consume(self, channel_name: str, callback: Callable):
        with self.__consume_conn.channel() as channel:
            try:
                channel.queue_declare(queue=channel_name)
                channel.basic_consume(
                    queue=channel_name, on_message_callback=callback, auto_ack=True
                )
                channel.start_consuming()
            except Exception as e:
                print(e)


rabbit_mq_instant = RabbitMQClient(server_settings.MQ_ADDRESS)
