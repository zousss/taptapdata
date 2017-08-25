# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
import json
import scrapy
from scrapy.http import HtmlResponse
import time
import re
from taptapData.items import TaptapdataItem,GamedataItem
import urllib
from scrapy.conf import settings
import pymysql

class ninegameSpider(CrawlSpider):
    #爬虫名称，同一个项目中要保持唯一
    name = "freq_taptap"
    #初始url，该url在爬虫启动时会传给start_request，默认的回调函数是parse
    start_urls = ['https://www.taptap.com/ajax/tag/hot-list']

    #链接数据库
    def __init__(self):
        self.connect = pymysql.connect(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            use_unicode= True,
        )
        self.cursor = self.connect.cursor()

    #获取游戏链接
    def get_game_link(self):
        sql = 'select game_link,game_type from taptap_gameinfo group by game_link,game_type'
        self.cursor.execute(sql)
        games = self.cursor.fetchall()
        return games


    #根据初始链接，获取
    def parse(self,response):
        #xpath提取页面数据,利用标签树的路径取到想要的标签对象
        #https://www.taptap.com/search/tags?kw=%E8%A7%92%E8%89%B2%E6%89%AE%E6%BC%94&sort=updated
        #https://www.taptap.com/search/tags?kw=%E8%A7%92%E8%89%B2%E6%89%AE%E6%BC%94

        #先收集游戏数据
        if re.search(r'page',response.url):
            tgames = self.get_game_link()
            for tgame in tgames:
                game_info = scrapy.Request(tgame[0],callback=self.parse_game_data)
                game_info.meta['game_type'] = tgame[1]
                yield game_info

        content = HtmlResponse(url =response.url,body = json.loads(response.body_as_unicode())['data']['html'].strip().encode('utf-8'))
        for type_link in content.xpath('//div[@class="section-title"]/a/@href').extract():
            freq_type_link = type_link+'&sort=updated'
            games = scrapy.Request(freq_type_link,callback=self.get_games)
            yield games
        next_page = json.loads(response.body_as_unicode())['data']['next']
        if next_page:
            next_games = scrapy.Request(next_page,callback=self.parse)
            yield next_games

    #获取该类别下第一页的所有游戏链接
    def get_games(self,response):
        print '[TYPE LINK]:',response.url
        game_type = response.xpath('//div[@class="container"]/div/div/section[1]/header/div[1]/h1/text()').extract()[0]
        for game_link in response.xpath('//*[@id="searchList"]/div[@class="taptap-app-card"]/a/@href').extract():
            game_info = scrapy.Request(game_link,callback=self.parse_game)
            game_info.meta['game_type'] = game_type
            yield game_info

    #解析游戏链接
    def parse_game(self,response):
        print '###[GAME LINK]:',response.url
        taptapdataItem = TaptapdataItem()
        taptapdataItem['game_type'] = response.xpath('//div[@class="container"]/div/ol/li[3]/a/text()').extract()[0]
        taptapdataItem['game_link'] = response.url
        try:
            for game_info in response.xpath('//div[@class="container"]/div/div/section[1]'):
                taptapdataItem['game_name'] = ','.join(game_info.xpath('div[1]/div[2]/h1/text()').extract())
                taptapdataItem['game_img'] = ','.join(game_info.xpath('div[1]/div[1]/div/img/@src').extract())
                taptapdataItem['game_size'] = ','.join(game_info.xpath('div[2]/div[7]/ul/li[1]/span[2]/text()').extract()) + ','.join(game_info.xpath('div[2]/div[6]/ul/li[1]/span[2]/text()').extract())+ ','.join(game_info.xpath('div[2]/div[5]/ul/li[1]/span[2]/text()').extract())+ ','.join(game_info.xpath('div[2]/div[4]/ul/li[1]/span[2]/text()').extract())
                taptapdataItem['game_package'] = ','.join(game_info.xpath('div[1]/div[2]/div[2]/div[2]/@data-app-identifier').extract())
                taptapdataItem['game_version'] = ','.join(game_info.xpath('div[2]/div[7]/ul/li[2]/span[2]/text()').extract()) + ','.join(game_info.xpath('div[2]/div[6]/ul/li[2]/span[2]/text()').extract()) + ','.join(game_info.xpath('div[2]/div[5]/ul/li[2]/span[2]/text()').extract())+ ','.join(game_info.xpath('div[2]/div[4]/ul/li[2]/span[2]/text()').extract())
                taptapdataItem['game_updatetime'] = ','.join(game_info.xpath('div[2]/div[7]/ul/li[3]/span[2]/text()').extract()) + ','.join(game_info.xpath('div[2]/div[6]/ul/li[3]/span[2]/text()').extract()) + ','.join(game_info.xpath('div[2]/div[5]/ul/li[3]/span[2]/text()').extract())+ ','.join(game_info.xpath('div[2]/div[4]/ul/li[3]/span[2]/text()').extract())
            taptapdataItem['game_tag'] = ','.join(response.xpath('//*[@id="appTag"]/li/a/text()').extract()).strip().replace(' ','').replace('\t','')
            taptapdataItem['game_desc'] = ','.join(response.xpath('//*[@id="description"]/text()').extract()).strip().replace(' ','').replace('\t','')
            taptapdataItem['record_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            yield taptapdataItem
        except:
            print '[ERROR LINK]:',response.url

    #解析游戏数据
    def parse_game_data(self,response):
        print '###[GAME DATA]:',response.url
        gamedataItem = GamedataItem()
        gamedataItem['game_type'] = response.meta['game_type']
        try:
            for game_info in response.xpath('//div[@class="container"]/div/div/section[1]'):
                gamedataItem['game_name'] = ','.join(game_info.xpath('div[1]/div[2]/h1/text()').extract())
                #gamedataItem['game_rate'] = ','.join(game_info.xpath('div[1]/div[2]/div[2]/div[1]/p/span/text()').extract())
                gamedataItem['game_rate'] = ','.join(game_info.xpath('div[1]/span/span/span/text()').extract()) if game_info.xpath('div[1]/span/span/span/text()').extract() else 0
                gamedataItem['game_downloadnum'] = re.search(r'(\d+)\D',','.join(game_info.xpath('div[1]/div[2]/div[2]/div[1]/span/text()').extract())).group(1)
                gamedataItem['game_commentnum'] = ','.join(game_info.xpath('div[1]/div[3]/ul/li[2]/a/small/text()').extract()) if ','.join(game_info.xpath('div[1]/div[3]/ul/li[2]/a/small/text()').extract()) else 0
                gamedataItem['game_topicnum'] = ','.join(game_info.xpath('div[1]/div[3]/ul/li[3]/a/small/text()').extract()) if ','.join(game_info.xpath('div[1]/div[3]/ul/li[3]/a/small/text()').extract()) else 0
            gamedataItem['record_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            yield gamedataItem
        except:
            print '[ERROR LINK]:',response.url