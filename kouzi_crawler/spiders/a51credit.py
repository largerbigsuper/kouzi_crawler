# -*- coding: utf-8 -*-
import scrapy
from kouzi_crawler.items import KouziCrawlerItem

class A51creditSpider(scrapy.Spider):
    name = '51credit'
    allowed_domains = ['51credit.com']
    start_urls = ['https://www.51credit.com/loan/']

    def parse(self, response):
        app_list = response.xpath('//div[contains(@class,"loan-wrap")]/div[@class="loan-list"]')
        kouzi_name = '我爱卡'
        kouzi_link = 'https://www.51credit.com/loan/' 
        kouzi_type = 'web'
        for item in app_list:
            app_item = KouziCrawlerItem()
            name = item.xpath('./a/h2/text()').extract_first()
            if(name is None):
                continue
            app_item['app_name'] = name.strip()
            app_item['kouzi_type'] = kouzi_type
            app_item['kouzi_name'] = kouzi_name
            app_item['kouzi_link'] = kouzi_link
            app_link = item.xpath('./a/@href').extract_first()
            yield scrapy.Request(app_link, meta={'app_item':app_item}, callback=self.parse_app_link)

    def parse_app_link(sele, response):
        app_item = response.meta['app_item']
        app_item['app_link'] = response.url
        yield app_item