import sys
sys.path.append('.\\chef_spyder\\toutiao')

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from chef_spyder.toutiao import settings as toutiao_settings
from chef_spyder.toutiao.toutiao_spyder import TouTiaoSpider

from chef_nats.client import NatsClient
from chef_utility import hotspyder_utility
import asyncio
import uvicorn
from fastapi import FastAPI

import server_settings



def init_nats():
    try:
        natsClient = NatsClient()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(natsClient.run())
        loop.run_forever()
    except Exception as e:
        loop.close()


if __name__ == "__main__":
    hotspyder_utility.THREAD_POOL.submit(init_nats)

    server_settings = Settings()
    server_settings.setmodule(toutiao_settings)

    process = CrawlerProcess(server_settings)
    process.crawl(TouTiaoSpider, task_id="1234234")
    process.start()

    pass

    # uvicorn.run(
    #     "main:app", port=settings.UVICRON_PORT, log_level=settings.UVICRON_LOG_LEVEL
    # )
