# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import time
from kouzi_crawler.settings import MONGO_HOST,MONGO_PORT,MONGO_DB_NAME,MONGO_DB_CRAWL_COLLECTION

class KouziCrawlerPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(host=MONGO_HOST,port=MONGO_PORT)
        db = client[MONGO_DB_NAME]
        self.collection = db[MONGO_DB_CRAWL_COLLECTION]

    def process_item(self, item, spider):
        item['insert_at'] = time.time()
        data = dict(item)
        self.collection.update_one({
            'kouzi_name': data['kouzi_name'],
            'app_name': data['app_name'],
            'app_link': data['app_link']
        },{'$set':data},upsert=True)
        return item