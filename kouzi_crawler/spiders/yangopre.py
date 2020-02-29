# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from kouzi_crawler.items import KouziCrawlerItem

class YangopreSpider(CrawlSpider):
    name = 'yangopre'
    allowed_domains = ['yangopre.com']
    start_urls = ['http://1.yangopre.com/']

    rules = (
        Rule(LinkExtractor(allow=r'\/index\/index\/index\/type\/(\d+).html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        app_list = response.xpath('//ul[@class="loan-list"]/li[@class="active"]//ul[@class="item-list"]//li')
        kouzi_name = response.xpath('//title/text()').extract_first()
        kouzi_link = response.url 
        kouzi_type = 'web'
        for item in app_list:
            app_item = KouziCrawlerItem()
            app_item['app_name'] = item.xpath('.//div[@class="name"]/text()').extract_first().strip()
            app_item['app_link'] = item.xpath('./a/@href').extract_first()
            app_item['kouzi_type'] = kouzi_type
            app_item['kouzi_name'] = kouzi_name
            app_item['kouzi_link'] = kouzi_link
            yield app_item
