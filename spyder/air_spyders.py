import requests
from bs4 import BeautifulSoup
from typing import Callable, Optional, Any
from spyder_status import SpyderStatus


class AirSpyder:

    def __init__(self, start_url: str, cb: Optional[Callable] | None):
        self.__start_url = start_url
        self.__callback = cb
        self.__status = SpyderStatus.INITIATED

    @property
    def start_url(self):
        return self.__start_url
    
    @property
    def status(self):
        return self.__status

    def request(self):
        
        with requests.session().get(url=self.__start_url) as resp:
            soup = BeautifulSoup(resp.text, "lxml")
            if not callable(self.__callback) or self.__callback is None:
                self.parser(soup)
            else:
                self.__callback(soup)

    def parser(self, soup: BeautifulSoup):
        print(soup.select(".idx_cm_list li"))

    def run(self):
        try:
            self.request()
        except Exception as e:
            print(e)


class WangYiAirSpyder(AirSpyder):

    def __init__(self, start_url: str, cb: Callable[..., Any] | None):
        super().__init__(start_url, cb)

    def parser(self, soup: BeautifulSoup):
        print(soup.select(".idx_cm_list li"))


if __name__ == "__main__":
    WangYiAirSpyder("https://news.163.com/domestic/", cb=None).run()
