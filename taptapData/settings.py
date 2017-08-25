# -*- coding: utf-8 -*-

# Scrapy settings for taptapData project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import random

BOT_NAME = 'taptapData'

SPIDER_MODULES = ['taptapData.spiders']
NEWSPIDER_MODULE = 'taptapData.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'taptapData (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
LOG_LEVEL = 'WARNING'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = random.uniform(0,1)
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False
def getCookie():
    cookie_list = [
        'acw_tc=AQAAAJqwAwd84QkAIsXgel92jatQOlqw; locale=eyJpdiI6IjFJOURhT3A2T3hIXC91R1MzbVZHQ2ZBPT0iLCJ2YWx1ZSI6IjF0TmJhRTdrRWdUeVplNTdaa0o3YlE9PSIsIm1hYyI6IjNjNTYwYmZjNDY3YTA0ZTdkN2E5MDNjZTVhMmYzZWI2Y2MwMzIzMDg2OTJmNmU0ZWVhZTU3ZGRkMDBlZjhlNzcifQ%3D%3D; tapadid=e98be787-c087-c939-dd5b-dad3218352d7; bottom_banner_hidden=1; video_muted=1; XSRF-TOKEN=eyJpdiI6ImxxOENrWWlGUGdZMEE2WGQ1V2ExeVE9PSIsInZhbHVlIjoiVHJDTlV2eDBTS3NMR1hQbTVwWXRNZkJWNVIrWWlic0N5b3dQXC9RNldKbmZtQVFVVlpZck1VTzh6XC8wUWhNR3pCVW51WHIyUk51YnUrY1RUdThYNFVEQT09IiwibWFjIjoiYWNlNjA0ZDNmZjY5YTBiOTNjMmVjYjg2OTIzODk0ZjJhY2ExMTcxMmZmNmVlY2U2NWExNGVmYTE3NjFlODI4NCJ9; tap_sess=eyJpdiI6Iis5M1NSV3Vkcm10Y09PS1wvdkpuXC9CQT09IiwidmFsdWUiOiJHYlVPTTNiRzUyczFyUFl2WjVUWGVDekJPVDRsZ2t4ZWloN3RFODA3bXY3Q0dGd0MzYUxzdTRnR3FSYzdOalpSemttZVFpKzJIU0xGSlJheVwvaE9mZlE9PSIsIm1hYyI6ImQyYTcxYzA0NjhlNGY1Nzg0ZWY5YjMwOTZkMWJjZWQ3NDdkY2UyZjUzM2IxZDA1MWE0ZWMzMTE0MTk4MjQ3ZGMifQ%3D%3D; _ga=GA1.2.1493516884.1491888622',
        'acw_tc=AQAAAJqwAwd84QkAIsXgel92jatQOlqw; locale=eyJpdiI6IjFJOURhT3A2T3hIXC91R1MzbVZHQ2ZBPT0iLCJ2YWx1ZSI6IjF0TmJhRTdrRWdUeVplNTdaa0o3YlE9PSIsIm1hYyI6IjNjNTYwYmZjNDY3YTA0ZTdkN2E5MDNjZTVhMmYzZWI2Y2MwMzIzMDg2OTJmNmU0ZWVhZTU3ZGRkMDBlZjhlNzcifQ%3D%3D; tapadid=e98be787-c087-c939-dd5b-dad3218352d7; bottom_banner_hidden=1; video_muted=1; _ga=GA1.2.1493516884.1491888622; XSRF-TOKEN=eyJpdiI6InpwRFIyM2RXdUpFTFZueHN1Y1hCZUE9PSIsInZhbHVlIjoiZ2tRa0U2SEdydFJqUUtIdjJidmVLZEFEcnNVTVdkNDZ3cXp3S1UwZXFNbFwvVEhqVHpmQTU3R3dFZUJcL0YrNnF3MktBQjRaQ2xRTlpucWJ3NEJuWFN2dz09IiwibWFjIjoiZDBkZGZlZjQ4MGI4ZjYzZmVjZTdjOWNiY2Y4M2JmYmIzOTJjZjJmZWUzNjg1MWQ4YWVjM2I1Nzg0MTU1OTdkZSJ9; tap_sess=eyJpdiI6IndqeXlOMTFsRHZoNW1NaGtPTktrUGc9PSIsInZhbHVlIjoidHVtbE9kRlFRZVFIN3lvUjFlenJHZ3FkalBEY29HTXFQTzVFNVh4MFZzNlllVlBzSm96bnUyZkFOQ3pyQ1AzZEozck1HeXdLQ01rVmhwZ2xXSWI1Ync9PSIsIm1hYyI6ImZjODJiZWYzZjllOWM5ZGRmM2U3OGQ5MmNjYmVmNzlmYjIwYzk0OTZmNjU4NjU5NDNiMjg4MmE3ODgxODM1ZTAifQ%3D%3D'
    ]
    cookie = random.choice(cookie_list)
    return cookie

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, sdch, br",
    "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
    "Connection":"keep-alive",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36",
    'Cookie':'%s' % getCookie()
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'taptapData.middlewares.TaptapdataSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'taptapData.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'taptapData.pipelines.TaptapdataPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# start MySQL database configure setting
MYSQL_HOST = '192.168.112.47'
MYSQL_DBNAME = 'spiderdata'
MYSQL_USER = 'zoujianwei'
MYSQL_PASSWD = 'KPhUIEd2t622uwtB1xtZ'
# end of MySQL database configure setting
