# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from kouzi_crawler.items import KouziCrawlerItem


class JyudSpider(CrawlSpider):
    name = 'jyud'
    allowed_domains = ['jyud.cn']
    start_urls = ['http://www.jyud.cn/']

    rules = (
        Rule(LinkExtractor(allow=r'\/(.*?)'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        app_list = response.xpath('//div[@class="list_content"]//ul[@class="clearfix"]/li')
        kouzi_name = '借亦有道'
        kouzi_link = response.url 
        kouzi_type = 'web'
        for item in app_list:
            app_item = KouziCrawlerItem()
            app_item['app_name'] = item.xpath('./a//div[@class="rt"]//h2/text()').extract_first().strip()
            app_item['app_link'] = item.xpath('./a/@href').extract_first()
            app_item['kouzi_type'] = kouzi_type
            app_item['kouzi_name'] = kouzi_name
            app_item['kouzi_link'] = kouzi_link
            yield app_item
