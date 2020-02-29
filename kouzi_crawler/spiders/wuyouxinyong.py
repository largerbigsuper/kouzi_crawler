# -*- coding: utf-8 -*-
import scrapy
import json
from kouzi_crawler.items import KouziCrawlerItem


class WuyouxinyongSpider(scrapy.Spider):
    name = 'wuyouxinyong'
    allowed_domains = ['wuyouxinyong.com']
    start_urls = ["https://www.wuyouxinyong.com/banka/category-access/v1/find-category-list?app_id=205&platform=1&device_id=5506627&category_ids=" + str(x) for x in range(36, 40)]
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS':{
            'Host': 'www.wuyouxinyong.com',
            'Referer': 'https://www.wuyouxinyong.com/daikuan',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
    }
    def parse(self, response):
        kouzi_name = '口子大神'
        kouzi_link = 'https://www.wuyouxinyong.com/daikuan'
        kouzi_type = 'web'
        response_json = json.loads(response.body)
        app_list = response_json['result'][0]['card_link_list']
        for item in app_list:
            app_item = KouziCrawlerItem()
            app_item['app_name'] = item['platform_name']
            app_item['app_link'] = item['ios_url']
            app_item['kouzi_type'] = kouzi_type
            app_item['kouzi_name'] = kouzi_name
            app_item['kouzi_link'] = kouzi_link
            yield app_item
