
import sys
sys.path.append('.\\spyder')
sys.path.append('.\\spyder\\toutiao')
sys.path.append('.\\spyder\\common')
sys.path.append('.\\chef_nats\\')

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from spyder.toutiao import settings as toutiao_settings
from spyder.toutiao.toutiao_spyder import TouTiaoSpider



if __name__ == "__main__":
    settings = Settings()
    settings.setmodule(toutiao_settings)
    process = CrawlerProcess(settings=settings)
    process.crawl(TouTiaoSpider, task_id = '23342344')
    process.start()