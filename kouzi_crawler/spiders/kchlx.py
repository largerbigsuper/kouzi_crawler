# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from kouzi_crawler.items import KouziCrawlerItem

class KchlxSpider(CrawlSpider):
    name = 'kchlx'
    allowed_domains = ['zx3.kchlx.com']
    url = 'http://zx3.kchlx.com/plus/view.php?aid='
    index = 380
    start_urls = [url + str(index)]

    def parse(self, response):
        if response.status != 200:
            if self.index > 1:
                self.index -= 1

            # 每次处理完一页的数据之后，重新发送下一页页面请求
            # self.offset自增10，同时拼接为新的url，并调用回调函数self.parse处理Response
            yield scrapy.Request(self.url + str(self.index), callback = self.parse)
        else:
            app_name = response.xpath('//div[@class="news_box"]/h2/text()').extract_first()
            if app_name is not None:
                app_item = KouziCrawlerItem()
                app_item['app_name'] = app_name
                app_item['app_link'] = self.url + str(self.index)
                app_item['kouzi_type'] = 'web'
                app_item['kouzi_name'] = '分销平台'
                app_item['kouzi_link'] = 'http://zx3.kchlx.com/'
                yield app_item

            if self.index > 1:
                self.index -= 1

            # 每次处理完一页的数据之后，重新发送下一页页面请求
            # self.offset自增10，同时拼接为新的url，并调用回调函数self.parse处理Response
            yield scrapy.Request(self.url + str(self.index), callback = self.parse)

        
