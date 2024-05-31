from typing import Any, Iterable
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import Response
from bs4 import BeautifulSoup
from scrapy.settings import Settings
import settings as toutiao_settings
import requests

class TouTiaoSpider(scrapy.Spider):
    name = "TouTiaoSpider"
    hot_list_api = "https://api.vvhan.com/api/hotlist/toutiao"

    def __init__(self, name: str | None = None, **kwargs: Any):
        super().__init__(name, **kwargs)

        self.__hot_list = self.__init_urls()

    def __init_urls(self):
        request_items = [] 
        with requests.session().get(self.hot_list_api) as resp:
            data = resp.json()['data']
            print(data)
            if data is None or len(data) == 0:
                raise Exception('toutiao hot list response is empty')
            
            for item in data:
                request_items.append({'title':item['title'], 'url': item['url']})

        return request_items
    
    def start_requests(self) -> Iterable[scrapy.Request]:
        for item in self.__hot_list[:1]:
            yield scrapy.Request(url=item['url'], callback=self.parse)
    
    def parse(self, response: Response, **kwargs: Any):
        soup = BeautifulSoup(response.text, 'lxml')
        




if __name__ == '__main__':
    settings = Settings()
    settings.setmodule(toutiao_settings)
    process = CrawlerProcess(settings=settings)
    process.crawl(TouTiaoSpider)
    process.start()
