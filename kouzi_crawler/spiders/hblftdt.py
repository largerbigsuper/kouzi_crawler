# -*- coding: utf-8 -*-
import scrapy
from kouzi_crawler.items import KouziCrawlerItem

class A51creditSpider(scrapy.Spider):
    name = 'hblftdt'
    allowed_domains = ['hblftdt.com']
    start_urls = ['http://hblftdt.com/mobile/index/index.html']

    def parse(self, response):
        app_list = response.xpath('//ul//li')
        kouzi_name = '十一钱包'
        kouzi_link = response.url 
        kouzi_type = 'web'
        for item in app_list:
            app_item = KouziCrawlerItem()
            name = item.xpath('.//div/text()').extract_first()
            app_link = item.xpath('./a/@href').extract_first()
            app_item['app_name'] = name.strip()
            app_item['kouzi_type'] = kouzi_type
            app_item['kouzi_name'] = kouzi_name
            app_item['kouzi_link'] = kouzi_link
            app_item['app_link'] = app_link
            print(app_item)
            yield app_item
