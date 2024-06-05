import pika
from chef_utility.hotspyder_utility import MQ_CHANNEL_CONSUMMING_POOL



class MQClient():
    
    def __init__(self, address: str) -> None:
        self.__addr = address
        self.__publish_conn: pika.BlockingConnection = None
        self.__consume_conn: pika.BlockingConnection = None
        
    def __init_connections(self):
        try:
            self.__publish_conn = pika.BlockingConnection(
                pika.ConnectionParameters(host=self.__addr)
            )
            self.__consume_conn = pika.BlockingConnection(
                pika.ConnectionParameters(host=self.__addr)
            )

        except Exception as e:
            print(e)


__publish_conn: pika.BlockingConnection = None
__consume_conn: pika.BlockingConnection = None


def __init_MQ():
    global __publish_conn
    global __consume_conn

    try:
        __publish_conn = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
        )
        __consume_conn = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
        )

    except Exception as e:
        print(e)


def send(
    channel_name: str,
    payload: str,
    properties: pika.BasicProperties,
    exchange: str = "",
):
    with __publish_conn.channel() as channel:
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


def start_consuming(channel_name: str):
    global __consume_conn

    with __consume_conn.channel() as channel:
        MQ_CHANNEL_CONSUMMING_POOL.submit(channel.start_consuming)


__init_MQ()
