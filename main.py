from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from chef_spyder.toutiao import settings as toutiao_settings
from chef_spyder.toutiao.toutiao_spyder import TouTiaoSpider
from chef_nats.client import NatsClient
from chef_utility import hotspyder_utility
import asyncio


def init_nats():
    natsClient = NatsClient()
    loop = asyncio.get_running_loop()
    loop.run_until_complete(natsClient.run())
    loop.run_forever()


if __name__ == "__main__":
    hotspyder_utility.THREAD_POOL.submit(init_nats)
    print("----------------")
