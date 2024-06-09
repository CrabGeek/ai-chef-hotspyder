import pika
import server_settings


class RabbitMQClient:

    def __init__(self, address: str) -> None:
        self.__addr = address

    def send(
        self,
        channel_name: str,
        payload: str,
        properties: pika.BasicProperties,
        exchange: str = "",
    ):
        try:
            with pika.BlockingConnection(
                pika.ConnectionParameters(host=self.__addr)
            ) as connection:
                with connection.channel() as channel:
                    channel.queue_declare(channel_name)
                    channel.basic_publish(
                        exchange=exchange,
                        routing_key=channel_name,
                        body=payload,
                        properties=properties,
                    )
        except Exception as e:
            # TODO: NEED TO LOG
            print(e)

    def consume(self, channel_name, cb):
        try:
            with pika.BlockingConnection(
                pika.ConnectionParameters(host=self.__addr)
            ) as connection:
                with connection.channel() as channel:
                    channel.queue_declare(queue=channel_name)
                    channel.basic_consume(
                        queue=channel_name, on_message_callback=cb, auto_ack=True
                    )
                    channel.start_consuming()
        except Exception as e:
            # TODO: NEED TO LOG
            print(e)


rabbit_mq_instant = RabbitMQClient(server_settings.MQ_ADDRESS)
