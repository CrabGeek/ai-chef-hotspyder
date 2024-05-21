from typing import Any, Iterable
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import Response

# class QuotesSpider(scrapy.Spider):
#     name = "quotes"

#     def start_requests(self):
#         yield scrapy.Request(url='https://www.baidu.com', callback=self.parse)

#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         filename = f'quotes-{page}.html'
#         with open(filename, 'wb') as f:
#             f.write(response.body)
#         self.log(f'Saved file {filename}')


# if __name__ == '__main__':
#     process = CrawlerProcess()

#     process.crawl(QuotesSpider)
#     process.start() # the script will block here until the crawling is finished\


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