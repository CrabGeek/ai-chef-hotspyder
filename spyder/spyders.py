from typing import Any, Iterable
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import Response

class WeBoSpider(scrapy.Spider):
    name = "WeboSpider"

    def start_requests(self):
        return
    
    def parse(self, response):
        return
    

class RedNotesSpider(scrapy.Spider):
    name = "RedNotesSpider"

    def start_requests(self):
        return
    

    def parse(self, response) :
        return
    

class TouTiaoSpider(scrapy.Spider):
    name = "TouTiaoSpider"

    start_urls = [
        "https://www.toutiao.com"
    ]
    
    def parse(self, response: Response, **kwargs: Any) -> Any:
        filename = 'quotes.html'
        with open(filename, 'wb') as f:
            f.write(response.body)


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(TouTiaoSpider)
    process.start()
