# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaptapdataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    game_name = scrapy.Field()
    game_img = scrapy.Field()
    game_link = scrapy.Field()
    game_developer = scrapy.Field()
    game_type = scrapy.Field()
    game_desc = scrapy.Field()
    game_tag = scrapy.Field()
    game_size = scrapy.Field()
    game_version = scrapy.Field()
    game_updatetime = scrapy.Field()
    game_package = scrapy.Field()
    record_time = scrapy.Field()

class GamedataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    game_name = scrapy.Field()
    game_rate = scrapy.Field()
    game_downloadnum = scrapy.Field()
    game_commentnum = scrapy.Field()
    game_topicnum = scrapy.Field()
    game_type = scrapy.Field()
    record_time = scrapy.Field()
