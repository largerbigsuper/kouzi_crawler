# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from kouzi_crawler.items import KouziCrawlerItem

class QzkeySpider(CrawlSpider):
    name = 'qzkey'
    allowed_domains = ['qzkey.com']
    start_urls = ['http://mimi1688.aly611.qzkey.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Product.aspx\?typeid=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        app_list = response.xpath('//dl[@class="cpDl2"]/dd/ul//li')
        kouzi_name = '有鱼汇'
        kouzi_link = response.url 
        kouzi_type = 'web'
        for item in app_list:
            app_item = KouziCrawlerItem()
            app_item['app_name'] = item.xpath('./a//dd//h3/text()').extract_first().strip()
            app_item['app_link'] = item.xpath('./a/@href').extract_first()
            app_item['kouzi_type'] = kouzi_type
            app_item['kouzi_name'] = kouzi_name
            app_item['kouzi_link'] = kouzi_link
            yield app_item
