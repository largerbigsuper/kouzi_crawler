# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from kouzi_crawler.items import KouziCrawlerItem


class XingyuanhuibaoSpider(CrawlSpider):
    name = 'xingyuanhuibao'
    allowed_domains = ['xingyuanhuibao.com']
    start_urls = ['https://www.xingyuanhuibao.com/']

    rules = (
        Rule(LinkExtractor(allow=r'\/a\/shop\/.*?'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        body = response.body.decode('utf-8')
        response = response.replace(body=body)
        app_list = response.xpath(
            '//div[contains(@class,"indexbox")]/ul[@class="clearfix"]//li')
        kouzi_name = response.xpath('//title/text()').extract_first()
        kouzi_name = kouzi_name
        kouzi_link = response.url
        kouzi_type = 'web'
        for item in app_list:
            app_item = KouziCrawlerItem()
            app_name = item.xpath('./a/text()').extract_first()
            if(app_name is None):
                continue
            app_item['app_name'] = app_name.strip()
            app_item['app_link'] = item.xpath('./a/@href').extract_first()
            app_item['kouzi_type'] = kouzi_type
            app_item['kouzi_name'] = kouzi_name
            app_item['kouzi_link'] = kouzi_link
            yield app_item
