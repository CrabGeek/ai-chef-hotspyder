import json
from itemadapter import ItemAdapter
from chef_utility import hotspyder_utility
from chef_mq import instant
import pika
from pika.delivery_mode import DeliveryMode


class TouTiaoPipeline:

    def process_item(self, item, spider):
        data = json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False) + "\n"
        instant.send(
            channel_name="hotspyder_to_doorman",
            payload=data,
            properties=pika.BasicProperties(delivery_mode=DeliveryMode.Transient),
        )
        return item
