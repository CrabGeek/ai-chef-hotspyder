from typing import Any, Iterable
import scrapy
from scrapy.http import Response
from bs4 import BeautifulSoup
import scrapy.signals
import requests
from chef_spyder.common.items import CommonItem, Payload
import uuid


class TouTiaoSpider(scrapy.Spider):
    name = "TouTiaoSpider"
    hot_list_api = "https://api.vvhan.com/api/hotlist/toutiao"

    def __init__(
        self, task_id: str, prompt_words: str, name: str | None = None, **kwargs: Any
    ):
        super().__init__(name, **kwargs)
        self.__task_id = task_id
        self.__prompt_words = prompt_words
        self.__hot_list = self.__init_urls()
        # [self.__init_urls()[28]]

    def __init_urls(self):
        request_items = []
        with requests.session().get(self.hot_list_api) as resp:
            data = resp.json()["data"]
            if data is None or len(data) == 0:
                raise Exception("toutiao hot list response is empty")

            for item in data:
                request_items.append({"title": item["title"], "url": item["url"]})

        return request_items

    @property
    def task_id(self):
        return self.__task_id

    def start_requests(self) -> Iterable[scrapy.Request]:
        self.logger.info(f"starting with task id: [{self.__task_id}]")
        for item in self.__hot_list:
            yield scrapy.Request(
                url=item["url"],
                callback=self.parse_hot_portal,
                cb_kwargs={"title": item["title"]},
                meta={"middleware": "TouTiaoHotListPageDownloaderMiddleware"},
            )

    def parse_hot_portal(self, response: Response, title: str):
        soup = BeautifulSoup(response.text, "lxml")
        target_divs = soup.select(".feed-card-article-l")

        if target_divs is None or len(target_divs) == 0:
            self.logger.warning(
                f"title: [{title}], url: [{response.url}] is not article."
            )
            return

        target_div = target_divs[0]
        link = target_div.a.attrs["href"]

        if link is not None and "article" in link:
            self.logger.info(
                f"parser link from portal page with title: [{title}], link: [{link}]"
            )
            yield scrapy.Request(
                url=link,
                callback=self.extract_article,
                cb_kwargs={"title": title},
                meta={"middleware": "TouTiaoArticleDownloaderMiddleware"},
            )

    def extract_article(self, response: Response, title: str):
        soup = BeautifulSoup(response.text, "lxml")
        article_content = soup.select(".article-content")[0]

        if article_content is None:
            self.logger.warning(
                f"title: [{title}], url: [{response.url}], article is empty."
            )
            return

        item = CommonItem()
        item["task_id"] = self.__task_id
        item["url"] = response.url
        item["prompt_words"] = self.__prompt_words
        item["content_id"] = str(uuid.uuid4())

        payload = Payload()
        payload["title"] = title
        payload["content"] = article_content.text

        item["payload"] = payload

        yield item

        # with open(f"article-{random.randint(1, 30)}.txt", "+a", encoding="utf-8") as f:
        #         f.write(article_content.text)

    def closed(self, resaon):
        pass
        # TODO: trigger NATS send scrapy status
