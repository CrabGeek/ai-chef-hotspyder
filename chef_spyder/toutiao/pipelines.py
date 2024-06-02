import json
from itemadapter import ItemAdapter
from chef_nats.client import NatsClient
from chef_utility import hotspyder_utility
import asyncio
import nest_asyncio

nest_asyncio.apply()

class TouTiaoPipeline:

    def process_item(self, item, spider):
        print("-----------------------------")
        data = json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False) + "\n"
        # hotspyder_utility.THREAD_POOL.submit(
        #     lambda ctx: NatsClient.send(*ctx),
        #     ("foo", str.encode(data, encoding="utf-8")),
        # )

        asyncio.run(NatsClient.send("foo", str.encode(data, encoding="utf-8")))
        print("-----------------------------")
        return item
