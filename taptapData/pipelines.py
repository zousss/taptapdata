# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.conf import settings
from taptapData.items import TaptapdataItem,GamedataItem

class TaptapdataPipeline(object):
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

    def process_item(self, item, spider):
        if item.__class__ == TaptapdataItem:
            try:
                sql1 = 'REPLACE INTO taptap_gameinfo VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                param1 = (item['game_name'],item['game_link'],item['game_img'],item['game_type'],item['game_tag'], \
                         item['game_desc'],item['game_size'], \
                         item['game_version'],item['game_updatetime'], item['game_package'],\
                         item['game_rate'],item['game_downloadnum'],item['game_commentnum'],item['game_topicnum'], \
                         item['record_time'])
                self.cursor.execute(sql1,param1)
                self.connect.commit()
            except pymysql.Warning,w:
                print "Warning:%s" % str(w)
            except pymysql.Error, e:
                print "Error:%s" % str(e)
        if item.__class__ == GamedataItem:
            try:
                sql2 = 'INSERT INTO taptap_gamedata VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
                param2 = (item['game_link'],item['game_name'],item['game_type'],item['game_rate'],item['game_downloadnum'], \
                          item['game_commentnum'],item['game_topicnum'], item['record_time'])
                self.cursor.execute(sql2,param2)
                self.connect.commit()
            except pymysql.Warning,w:
                print "Warning:%s" % str(w)
            except pymysql.Error, e:
                print "Error:%s" % str(e)
        return item
