# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from .items import BbcItem
from . import settings



class BbcPipeline:

    def __init__(self):
        conn = pymongo.MongoClient(
                settings.MONGO_HOST,
                settings.MONGO_PORT

                )
        db = conn[settings.MONGO_DB_NAME]
        self.collection = db[settings.MONGO_COLLECTION_NAME]


    def process_item(self, item, spider):
        if isinstance(item, BbcItem):
                self.collection.insert_one(dict(item))
        return item
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(
                settings.MONGO_HOST,
                settings.MONGO_PORT
                )

    def close_spider(self, spider):
        self.client.close()
