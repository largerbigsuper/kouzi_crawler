# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from kouzi_crawler.items import KouziCrawlerItem


class Lu714Spider(CrawlSpider):
    name = 'lu714'
    allowed_domains = ['lu714.com']
    start_urls = ['http://www.lu714.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/plus/list.php\?tid=.*?'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        app_list = response.xpath('//div[@id="content"]/p[@id="mrtj"]//a')
        kouzi_name = '超级卡汇'
        kouzi_link = response.url 
        kouzi_type = 'web'
        for item in app_list:
            app_item = KouziCrawlerItem()
            name = item.xpath('./text()').extract_first()
            name = name.split('-')[0]
            app_item['app_name'] = name.strip()
            app_item['kouzi_type'] = kouzi_type
            app_item['kouzi_name'] = kouzi_name
            app_item['kouzi_link'] = kouzi_link
            app_detail_link = item.xpath('./@href').extract_first()
            yield scrapy.Request(self.start_urls[0]+app_detail_link, meta={'app_item':app_item}, callback=self.parse_app_link)

    def parse_app_link(sele, response):
        app_item = response.meta['app_item']
        app_item['app_link'] = response.url
        yield app_item