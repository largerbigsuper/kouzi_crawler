# -*- coding: utf-8 -*-
import json

import scrapy

from kouzi_crawler.items import KouziCrawlerItem

class LaogedailuSpider(scrapy.Spider):
    name = 'laogedailu'
    allowed_domains = ['laogedailu.com']
    start_urls = ['http://new.laogedailu.com/index/api/queryCustomer?pageSize=200&page=1']
    url_tpl = 'http://new.laogedailu.com/index/api/queryCustomer?pageSize=200&page={}'

    def parse(self, response):
        data = json.loads(response.text)['data']
        last_page = data['last_page']
        for page, _ in enumerate(range(last_page), 1):
            url = self.url_tpl.format(page)
            yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self, response):
        
        data = json.loads(response.text)['data']
        app_list = data['data']
        kouzi_name = '乐乐家APP'
        kouzi_link = response.url 
        kouzi_type = 'app'
        for item in app_list:
            app_item = KouziCrawlerItem()
            app_item['app_name'] = item['names']
            app_item['app_link'] = item['links']
            app_item['kouzi_type'] = kouzi_type
            app_item['kouzi_name'] = kouzi_name
            app_item['kouzi_link'] = kouzi_link
            
            # print(app_item)
            yield app_item