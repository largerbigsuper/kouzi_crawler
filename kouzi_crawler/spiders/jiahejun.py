# -*- coding: utf-8 -*-
import scrapy
import re
from kouzi_crawler.items import KouziCrawlerItem

class JiahejunSpider(scrapy.Spider):
    name = 'jiahejun'
    allowed_domains = ['jiahejun.com']
    start_urls = ['https://www.jiahejun.com/cc_daikuan-dk.html']

    def parse(self, response):
        app_list = response.xpath('//tbody[@id="daikuan_list"]//tr[@class="filter-tr"]')
        kouzi_name = '嘉合骏'
        kouzi_url = 'https://www.jiahejun.com/'
        kouzi_type = 'web'
        for item in app_list:
            app_item = KouziCrawlerItem()
            kouzi_detail = item.xpath('./td[@class="action"]//a/@href').extract_first()
            kouzi_id = re.match(r"kouzi-(\d+).html",kouzi_detail)
            kouzi_id = kouzi_id.group(1)
            name = item.xpath('./td[@class="logo"]//span/text()').extract_first()
            if(name is None):
                continue
            app_item['app_name'] = name.strip()
            app_item['app_link'] = '{}plugin.php?id=cc_daikuan:kz&kouziid={}'.format(kouzi_url,kouzi_id)
            app_item['kouzi_type'] = kouzi_type
            app_item['kouzi_name'] = kouzi_name
            app_item['kouzi_link'] = '{}{}'.format(kouzi_url,kouzi_detail)
            print(app_item)
            yield app_item

        next_link = response.xpath('//tbody[@id="daikuan_list"]//tr//div[@class="page"]//a[@class="nxt"]/@href').extract_first()
        if next_link:
            yield scrapy.Request(kouzi_url+next_link,callback=self.parse)