# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from kouzi_crawler.items import KouziCrawlerItem


class A1616888Spider(CrawlSpider):
    name = '1616888'
    allowed_domains = ['1616888.com']
    start_urls = ['https://www.1616888.com/']

    rules = (
        Rule(LinkExtractor(allow=r'link\?type=3&param=.*?'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        app_list = response.xpath('//div[@id="content"]/p[@id="mrtj"]//span')
        kouzi_name = response.xpath('//title/text()').extract_first()
        kouzi_link = response.url 
        kouzi_type = 'web'
        for item in app_list:
            app_item = KouziCrawlerItem()
            name = item.xpath('./a/text()').extract_first()
            name = name.split('-')[0]
            app_item['app_name'] = name.strip()
            app_item['app_link'] = item.xpath('./a/@href').extract_first()
            app_item['kouzi_type'] = kouzi_type
            app_item['kouzi_name'] = kouzi_name
            app_item['kouzi_link'] = kouzi_link
            yield app_item
