import json
from itemadapter import ItemAdapter
from chef_utility import hotspyder_utility
import chef_mq.client as mq_client
import pika
from pika.delivery_mode import DeliveryMode


class TouTiaoPipeline:

    def process_item(self, item, spider):
        data = json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False) + "\n"
        hotspyder_utility.THREAD_POOL.submit(
            lambda ctx: mq_client.send(*ctx),
            (
                "hotspyder_to_doorman",
                data,
                pika.BasicProperties(delivery_mode=DeliveryMode.Transient),
            ),
        )
        return item
