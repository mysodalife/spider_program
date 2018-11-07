# -*- coding: utf-8 -*-

# Scrapy settings for yunqiCrawl project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'yunqiCrawl'

SPIDER_MODULES = ['yunqiCrawl.spiders']
NEWSPIDER_MODULE = 'yunqiCrawl.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WinSH64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False # 网站不需要登录就可以爬取时 可以选择禁用 cookie

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
  'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
  'Accept-Encoding':'gzip, deflate, sdch',
  'Connection':'keep-alive',
  'Cache-Control':'no-cache',
  'Pragma':'no-cache',
  'Upgrade-Insecure-Requests':'1',
  'Host':'yunqi.qq.com',
  'referer':'yunqi.qq.com'
}
# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'yunqiCrawl.middlewares.YunqicrawlSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None, # 这里同时禁用
   'yunqiCrawl.middlewares.RandomUserAgent': 410,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'yunqiCrawl.pipelines.YunqicrawlPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay       # 这3个配置项都是为了进行反爬虫
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# MongoDB Configure
MONGODB_HOST = '222.199.193.65'
MONGODB_PORT = 27017
MONGODB_USERNAME = 'sodalife'
MONGODB_DATABASE = 'pythonSpider'



# User-Agent pool
USER_AGENTS = [
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64; ServiceUI 13.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
]

# redis 实现分布式爬虫 使用 scrapy_redis 的调度器 使用自己的调度器
SCHEDULER = 'scrapy_redis.scheduler.Scheduler'

# 在 redis 中保持 scrapy-redis 用到的各个队列中的，从而允许 暂停和暂停后恢复
SCHEDULER_PERSIST = True

# 使用 redis_redis 的去重方式 URL 去重
DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'

REDIS_HOST = '222.199.193.65'
REDIS_PORT = 6379

# 基于redis 在 redis中添加到 bloomfilter中
# FILTER_URL = None
# FILTER_HOST = '222.199.193.65'
# FILTER_PORT = 6379
# FILTER_DB = 0
# SCHEDULER_QUEUE_CLASS = 'yunqiCrawl.scrapy_redis.queue.SpiderPriorityQueue'