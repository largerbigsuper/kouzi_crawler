# -*- coding: utf-8 -*-
import scrapy
import re
import json
from kouzi_crawler.items import KouziCrawlerItem


class KanongquanSpider(scrapy.Spider):
    name = 'kanongquan'
    allowed_domains = ['kanongquan.net']
    start_urls = ['https://d.kanongquan.net/index.php?r=share%2Fdaikuan']

    def parse(self, response):
        app_list = response.xpath('//div[@id="content"]//ul/li')
        kouzi_name = '卡农联盟'
        url = 'https://d.kanongquan.net'
        kouzi_type = 'web'
        for item in app_list:
            app_item = KouziCrawlerItem()
            app_link = item.xpath('./a/@href').extract_first()
            app_item['kouzi_link'] = url + app_link
            app_item['kouzi_type'] = kouzi_type
            app_item['kouzi_name'] = kouzi_name
            kouzi_id = re.match(r".*?series_id=(\d+)",app_link)
            kouzi_id = kouzi_id.group(1)
            app_data_url = 'https://d.kanongquan.net/index.php?r=share%2Fmore&page=1&page_size=1000&series_id={}&class_id='.format(kouzi_id)
            yield scrapy.Request(app_data_url, meta={'app_item':app_item}, callback=self.parse_app_link)

    def parse_app_link(sele, response):
        app_item = response.meta['app_item']
        response_json = json.loads(response.body)
        app_list = response_json['datas']
        for item in app_list:
            app_item['app_name'] = item['title']
            app_item['app_link'] = item['url']
            yield app_item
