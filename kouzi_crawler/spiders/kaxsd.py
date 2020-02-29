# -*- coding: utf-8 -*-
import scrapy
import json
import re
from kouzi_crawler.items import KouziCrawlerItem

class KaxsdSpider(scrapy.Spider):
    name = 'kaxsd'
    allowed_domains = ['kaxsd.cn']
    start_urls = ['http://www.kaxsd.cn/']

    def parse(self, response):
        app_list = response.xpath('//div[@class="index_main_top"]/ul/li/a[@class="h2name"]')
        for item in app_list:
            cate1 = item.xpath('./@data-cate1').extract_first()
            cate2 = item.xpath('./@data-cate2').extract_first()
            yield scrapy.Request('http://www.kaxsd.cn/main_main/index?cate1={}&cate2={}&handle=ajax'.format(cate1,cate2), callback=self.parse_item)
            


    def parse_item(self, response):
        kouzi_name = '分销平台'
        kouzi_link = 'http://www.kaxsd.cn/' 
        kouzi_type = 'web'
        response_json = json.loads(response.body)
        page_html = response_json['data']
        app_list = scrapy.Selector(text=page_html).xpath('//li')
        for item in app_list:
            app_item = KouziCrawlerItem()
            name = item.xpath('./a/h1/text()').extract_first()
            if(name is None):
                continue
            app_item['app_name'] = name.strip()
            app_item['kouzi_type'] = kouzi_type
            app_item['kouzi_name'] = kouzi_name
            app_item['kouzi_link'] = kouzi_link
            app_item['app_link'] = item.xpath('./a/@href').extract_first()
            yield app_item
            # app_detail_link = item.xpath('./a/@href').extract_first()
            # yield scrapy.Request(self.start_urls[0]+app_detail_link, meta={'app_item':app_item}, callback=self.parse_app_link)

    # def parse_app_link(sele, response):
    #     app_item = response.meta['app_item']
    #     app_link = response.xpath('//div[@class="kz_btn_all"]//div[@class="right righttbtn"]/@onclick').extract_first()
    #     app_link = re.match(r"window.location.href = '(.*?)'", app_link)
    #     app_link = app_link.group(1)
    #     app_item['app_link'] = app_link
    #     yield app_item