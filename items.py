# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LotteryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    turn = scrapy.Field()
    dateOpen = scrapy.Field()
    dateClose = scrapy.Field()
    totalPrize = scrapy.Field()
    lotteryNumber = scrapy.Field()
    lotteryNumberSpecial = scrapy.Field()
