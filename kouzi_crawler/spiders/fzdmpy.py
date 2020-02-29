# -*- coding: utf-8 -*-
import scrapy
from kouzi_crawler.items import KouziCrawlerItem

class FzdmpySpider(scrapy.Spider):
    name = 'fzdmpy'
    allowed_domains = ['fzdmpy.com']
    start_urls = ['http://www.fzdmpy.com/Search/index.html']

    def parse(self, response):
        app_list = response.xpath('//div[@id="pretime"]/div//p//span/a')
        kouzi_name = '鲁多多'
        kouzi_link = response.url 
        kouzi_type = 'web'
        for item in app_list:
            app_item = KouziCrawlerItem()
            name = item.xpath('./span/strong/text()').extract_first()
            if(name is None):
                continue
            app_item['app_name'] = name.strip()
            app_item['app_link'] = item.xpath('./@href').extract_first()
            app_item['kouzi_type'] = kouzi_type
            app_item['kouzi_name'] = kouzi_name
            app_item['kouzi_link'] = kouzi_link
            yield app_item
