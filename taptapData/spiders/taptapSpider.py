# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
import json
import scrapy
from scrapy.http import HtmlResponse
import time
import re
from taptapData.items import TaptapdataItem
import urllib

class ninegameSpider(CrawlSpider):
    #爬虫名称，同一个项目中要保持唯一
    name = "taptap"
    #初始url，该url在爬虫启动时会传给start_request，默认的回调函数是parse
    start_urls = ['https://www.taptap.com/ajax/tag/hot-list']

    #根据初始链接，获取
    def parse(self,response):
        #xpath提取页面数据,利用标签树的路径取到想要的标签对象
        content = HtmlResponse(url =response.url,body = json.loads(response.body_as_unicode())['data']['html'].strip().encode('utf-8'))
        for type_link in content.xpath('//div[@class="section-title"]/a/@href').extract():
            games = scrapy.Request(type_link,callback=self.get_games)
            yield games
        next_page = json.loads(response.body_as_unicode())['data']['next']
        if next_page:
            next_games = scrapy.Request(next_page,callback=self.parse)
            yield next_games

    #获取该类别下第一页的所有游戏链接
    def get_games(self,response):
        print '[TYPE LINK]:',response.url
        game_type = urllib.unquote(re.search(r'.*kw\=(.*)$',response.url).group(1))
        for game_link in response.xpath('//*[@id="searchList"]/div[@class="taptap-app-card"]/a/@href').extract():
            game_info = scrapy.Request(game_link,callback=self.parse_game)
            game_info.meta['game_type'] = game_type
            yield game_info
        #获取下一页的链接
        next_game_info = response.xpath('//section[@class="taptap-button-more"]/button/@data-url').extract()
        if next_game_info:
            next_json_games = scrapy.Request(next_game_info[0],callback=self.get_json_games)
            yield next_json_games

    #获取该类别下剩余页的游戏链接
    def get_json_games(self,response):
        print '[JSON TYPE LINK]:',response.url
        game_type = urllib.unquote(re.search(r'.*kw=(.*?)&',response.url).group(1))
        content = HtmlResponse(url =response.url,body = json.loads(response.body_as_unicode())['data']['html'].strip().encode('utf-8'))
        for game_link in content.xpath('//a[@class="app-card-left"]/@href').extract():
            json_game_info = scrapy.Request(game_link,callback=self.parse_game)
            json_game_info.meta['game_type'] = game_type
            yield json_game_info
        next_json_link = json.loads(response.body_as_unicode())['data']['next']
        if next_json_link:
            next_json_games = scrapy.Request(next_json_link,callback=self.get_json_games)
            yield next_json_games

    #解析游戏链接
    def parse_game(self,response):
        print '###[GAME LINK]:',response.url
        taptapdataItem = TaptapdataItem()
        taptapdataItem['game_type'] = response.meta['game_type']
        taptapdataItem['game_link'] = response.url
        try:
            for game_info in response.xpath('//div[@class="container"]/div/div/section[1]'):
                taptapdataItem['game_name'] = ','.join(game_info.xpath('div[1]/div[2]/h1/text()').extract())
                taptapdataItem['game_img'] = ','.join(game_info.xpath('div[1]/div[1]/div/img/@src').extract())
                taptapdataItem['game_developer'] = ','.join(game_info.xpath('div[1]/div[2]/div[1]/a/span[2]/text()').extract())
                taptapdataItem['game_rate'] = ','.join(game_info.xpath('div[1]/div[2]/div[2]/div[1]/p/span/text()').extract())
                taptapdataItem['game_downloadnum'] = re.search(r'\D(\d+)\D',','.join(game_info.xpath('div[1]/div[2]/div[2]/div[1]/span[1]/text()').extract())).group(1)
                taptapdataItem['game_package'] = ','.join(game_info.xpath('div[1]/div[2]/div[2]/div[2]/@data-app-identifier').extract())
                taptapdataItem['game_commentnum'] = ','.join(game_info.xpath('div[1]/div[3]/ul/li[2]/a/small/text()').extract()) if ','.join(game_info.xpath('div[1]/div[3]/ul/li[2]/a/small/text()').extract()) else 0
                taptapdataItem['game_topicnum'] = ','.join(game_info.xpath('div[1]/div[3]/ul/li[3]/a/small/text()').extract()) if ','.join(game_info.xpath('div[1]/div[3]/ul/li[3]/a/small/text()').extract()) else 0
                taptapdataItem['game_size'] = ','.join(game_info.xpath('div[2]/div[7]/ul/li[1]/span[2]/text()').extract()) + ','.join(game_info.xpath('div[2]/div[6]/ul/li[1]/span[2]/text()').extract())+ ','.join(game_info.xpath('div[2]/div[5]/ul/li[1]/span[2]/text()').extract())+ ','.join(game_info.xpath('div[2]/div[4]/ul/li[1]/span[2]/text()').extract())
                taptapdataItem['game_version'] = ','.join(game_info.xpath('div[2]/div[7]/ul/li[2]/span[2]/text()').extract()) + ','.join(game_info.xpath('div[2]/div[6]/ul/li[2]/span[2]/text()').extract()) + ','.join(game_info.xpath('div[2]/div[5]/ul/li[2]/span[2]/text()').extract())+ ','.join(game_info.xpath('div[2]/div[4]/ul/li[2]/span[2]/text()').extract())
                taptapdataItem['game_updatetime'] = ','.join(game_info.xpath('div[2]/div[7]/ul/li[3]/span[2]/text()').extract()) + ','.join(game_info.xpath('div[2]/div[6]/ul/li[3]/span[2]/text()').extract()) + ','.join(game_info.xpath('div[2]/div[5]/ul/li[3]/span[2]/text()').extract())+ ','.join(game_info.xpath('div[2]/div[4]/ul/li[3]/span[2]/text()').extract())
            taptapdataItem['game_tag'] = ','.join(response.xpath('//*[@id="appTag"]/li/a/text()').extract()).strip().replace(' ','').replace('\t','')
            taptapdataItem['game_desc'] = ','.join(response.xpath('//*[@id="description"]/text()').extract()).strip().replace(' ','').replace('\t','')
            taptapdataItem['record_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            yield taptapdataItem
        except:
            print '[ERROR LINK]:',response.url