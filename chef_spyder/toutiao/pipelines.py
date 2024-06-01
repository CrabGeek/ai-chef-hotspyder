import json
from itemadapter import ItemAdapter

class TouTiaoPipeline:
    
    def process_item(self, item, spider):
        print("-----------------------------")
        datas = json.dumps(ItemAdapter(item).asdict(), ensure_ascii= False) + "\n"
        print(datas)
        print("-----------------------------")
        return item
