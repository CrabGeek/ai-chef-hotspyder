from typing import Any, Iterable
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import Response
from bs4 import BeautifulSoup

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
        "https://news.163.com/domestic/"
    ]
    
    def parse(self, response: Response, **kwargs: Any) -> Any:
        filename = 'quotes.html'
        scrapy.Request()
        with open(filename, 'wb') as f:
            f.write(response.body)


class WangYiSpider(scrapy.Spider):
    name = "WangYiSpider"

    start_urls = [
        "https://news.163.com/domestic/"
    ]
    
    def parse(self, response: Response, **kwargs: Any) -> Any:
        soup = BeautifulSoup(response.body, 'lxml')
        print(soup.select('.idx_cm_list li'))


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(WangYiSpider)
    process.start()
