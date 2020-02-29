# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class KouziCrawlerItem(Item):
    # 产品名字
    app_name = Field()
    # 产品推广链接
    app_link = Field()
    # 口子名称
    kouzi_name = Field()
    # 口子地址
    kouzi_link = Field()
    # 口子类型
    kouzi_type = Field()
    # 入库时间
    insert_at = Field()
