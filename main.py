import sys
sys.path.append('.\\chef_spyder\\toutiao')

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from chef_spyder.toutiao import settings as toutiao_settings
from chef_spyder.toutiao.toutiao_spyder import TouTiaoSpider

import uvicorn
from fastapi import FastAPI

import server_settings



if __name__ == "__main__":

    server_settings = Settings()
    server_settings.setmodule(toutiao_settings)

    process = CrawlerProcess(server_settings)
    process.crawl(TouTiaoSpider, task_id="1234234", prompt_words="生成评论, 300字")
    process.start()


    # uvicorn.run(
    #     "main:app", port=settings.UVICRON_PORT, log_level=settings.UVICRON_LOG_LEVEL
    # )
