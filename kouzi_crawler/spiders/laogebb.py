# -*- coding: utf-8 -*-
import scrapy
from kouzi_crawler.items import KouziCrawlerItem


class LaogebbSpider(scrapy.Spider):
    name = 'laogebb'
    allowed_domains = ['laogebb.cn']
    start_urls = ['http://www.laogebb.cn/index.php?app=search']

    def parse(self, response):
        app_list = response.xpath('//div[@id="content"]/p//a')
        kouzi_name = '老哥汇'
        kouzi_link = response.url 
        kouzi_type = 'web'
        for item in app_list:
            app_item = KouziCrawlerItem()
            name = item.xpath('./text()').extract_first()
            if(name is None):
                continue
            app_item['app_name'] = name.strip()
            app_item['app_link'] = item.xpath('./@href').extract_first()
            app_item['kouzi_type'] = kouzi_type
            app_item['kouzi_name'] = kouzi_name
            app_item['kouzi_link'] = kouzi_link
            yield app_item
            

