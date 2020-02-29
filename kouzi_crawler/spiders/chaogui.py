# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from kouzi_crawler.items import KouziCrawlerItem


class ChaoguiSpider(scrapy.Spider):
    name = 'chaogui'
    domain = 'http://chaogui.net'
    app_domain = 'http://chaogui.net/app/'
    allowed_domains = ['chaogui.net']
    start_urls = ['http://chaogui.net/app/list.php?tid=13&PageNo=1']

    crawed_page_ids = set()

    # rules = (
    #     Rule(LinkExtractor(allow=r'list.php\?tid=13&PageNo=.*?'), callback='parse', follow=True),
    # )

    def parse(self, response):
        page_id = int(response.url.split('=')[-1])
        print('crawed page_id : {}'.format(page_id))
        self.crawed_page_ids.add(page_id)

        app_list = response.xpath('//ul[@class="search-result-list"]/li')
        kouzi_name = '小七钱包'
        kouzi_link = response.url 
        kouzi_type = 'web'
        for item in app_list:
            app_item = KouziCrawlerItem()
            app_item['app_name'] = item.xpath('./a/div[@class="result-text"]/h2/text()').extract_first()
            app_item['app_link'] = self.app_domain + item.xpath('./a/@href').extract_first()
            app_item['kouzi_type'] = kouzi_type
            app_item['kouzi_name'] = kouzi_name
            app_item['kouzi_link'] = kouzi_link
            
            # print(app_item)
            yield app_item
        pages = response.xpath('//ul[@class="pagination"]//li[not (contains(@class, "active"))]//a/@href').extract()
        for url in pages:
            next_page = self.domain + url
            new_page_id = int(next_page.split('=')[-1])
            if not new_page_id in  self.crawed_page_ids:
                yield scrapy.Request(next_page,  callback=self.parse)

