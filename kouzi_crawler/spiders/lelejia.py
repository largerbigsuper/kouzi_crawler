# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from kouzi_crawler.items import KouziCrawlerItem


class LelejiaSpider(CrawlSpider):
    name = 'lelejia'
    allowed_domains = ['lelejia.top']
    start_urls = ['http://lelejia.top/']

    rules = (
        Rule(LinkExtractor(allow=r'\?fl=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        app_list = response.xpath('//section[@class="nr"]//a')
        kouzi_name = '乐乐家'
        kouzi_link = response.url 
        kouzi_type = 'web'
        for item in app_list:
            app_item = KouziCrawlerItem()
            app_item['app_name'] = item.xpath('.//div[@class="list_a3"]//p[@class="p1"]/text()').extract_first().strip()
            app_item['app_link'] = item.xpath('./@href').extract_first()
            app_item['kouzi_type'] = kouzi_type
            app_item['kouzi_name'] = kouzi_name
            app_item['kouzi_link'] = kouzi_link
            yield app_item
