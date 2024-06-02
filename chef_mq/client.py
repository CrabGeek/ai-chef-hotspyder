import pika
from chef_utility.hotspyder_utility import MQ_CHANNEL_CONSUMMING_POOL


MQ_CHANNEL_MAP = {}


def __init_MQ():
    try:
        conn = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
        channel = conn.channel()
        channel.queue_declare("hotspyder_to_doorman")
        MQ_CHANNEL_MAP.update({"hotspyder_to_doorman": channel})
    except Exception as e:
        print(e)


def send(channel_name: str, payload: str, properties: pika.BasicProperties):
    channel = MQ_CHANNEL_MAP.get(channel_name)
    if channel is None:
        # TODO: need to log
        return

    try:
        channel.basic_publish(
        exchange="", routing_key=channel_name, body=payload, properties=properties
    )
    except Exception as e:
        #TODO: need log
        print(e)


def start_consuming(channel_name: str):
    channel = MQ_CHANNEL_MAP.get(channel_name)
    if channel is None:
        # TODO: need to log
        return
    MQ_CHANNEL_CONSUMMING_POOL.submit(channel.start_consuming)


__init_MQ()
