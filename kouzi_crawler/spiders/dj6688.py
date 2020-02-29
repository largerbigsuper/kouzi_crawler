# -*- coding: utf-8 -*-
import scrapy
from kouzi_crawler.items import KouziCrawlerItem


class Dj6688Spider(scrapy.Spider):
    name = 'dj6688'
    allowed_domains = ['dj6688.com.cn']
    start_urls = ['https://www.dj6688.com.cn']

    def parse(self, response):
        app_list = response.xpath('//div[@class="rows"]/a')
        kouzi_name = '点金易推'
        kouzi_link = response.url 
        kouzi_type = 'web'
        for item in app_list:
            app_item = KouziCrawlerItem()
            name = item.xpath('.//div[@class="des"]/span/text()').extract_first()
            if(name is None):
                continue
            app_item['app_name'] = name.strip()
            app_item['app_link'] = self.start_urls[0] + item.xpath('./@href').extract_first()
            app_item['kouzi_type'] = kouzi_type
            app_item['kouzi_name'] = kouzi_name
            app_item['kouzi_link'] = kouzi_link
            yield app_item
