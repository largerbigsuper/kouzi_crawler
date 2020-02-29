# -*- coding: utf-8 -*-
import scrapy
import json
from kouzi_crawler.items import KouziCrawlerItem

class AdongSpider(scrapy.Spider):
    name = 'adong'
    allowed_domains = ['adong.ren']
    start_urls = ['http://adong.ren/main/achieve/cat_list']

    def parse(self, response):
        response_json = json.loads(response.body)
        cat_list = response_json['list']
        for item in cat_list:
            cat_id = str(item['cat_id'])
            yield scrapy.Request('http://adong.ren/main/achieve/card_list?cat_id=' + cat_id, callback=self.parse_item)

    def parse_item(self, response):
        response_json = json.loads(response.body)
        card_list = response_json['list']
        for item in card_list:
            app_item = KouziCrawlerItem()
            app_item['app_name'] = item['name']
            app_item['app_link'] = item['links']
            app_item['kouzi_type'] = 'web'
            app_item['kouzi_name'] = '大东与小丹'
            app_item['kouzi_link'] = 'http://adong.ren'
            yield app_item
