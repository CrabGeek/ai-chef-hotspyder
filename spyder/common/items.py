from scrapy.item import Item, Field

class Payload(Item):
    title = Field()
    content = Field()

class CommonItem(Item):
    task_id = Field()
    content_id = Field()
    url = Field()
    payload = Field()