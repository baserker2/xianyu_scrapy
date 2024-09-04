# Scrapy settings for scrapy_spider project
'''settings'''
# 2024.09.01


'''init'''
BOT_NAME = 'xianyu'
SPIDER_MODULES = ["xianyu.spiders"]
NEWSPIDER_MODULE = "xianyu.spiders"
ROBOTSTXT_OBEY = False

'''piplines'''
ITEM_PIPELINES = {
    # 'gitee.pipelines.RedisPipeline': 300,
    'scrapy_xianyu.xianyu.pipelines.XianyuSpiderPipeline': 300,
    # 'scrapy_xianyu.xianyu.pipelines.ScrapySpiderPipeline': 301,
}


'''UA'''
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}


'''REDIS 设置'''
SCHEDULER = "scrapy_redis.scheduler.Scheduler" # 1.启用调度将请求存储进redis  必须
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter" # 2.确保所有spider通过redis共享相同的重复过滤。  必须
REDIS_HOST = 'localhost' # 3.指定连接到Redis时要使用的主机和端口。  必须
REDIS_PORT = 6379
SCHEDULER_PERSIST = True # 可选  允许暂定,redis数据不丢失

'''MONGO 设置'''
MONGODB_HOST = 'localhost'  # MONGODB 主机环回地址127.0.0.1
MONGODB_PORT = 27017  # 端口号，默认是27017
MONGODB_DBNAME = 'Gitee'  # 设置数据库名称
MONGODB_DOCNAME = 'test'  # 存放本次数据的表名称
MONGODB_DOCNAME2 = 'project'
'''qbs参数'''
# CONCURRENT_REQUESTS = 32 # 并发数
DOWNLOAD_DELAY = 1 # 发送间隔
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

'''middlewares'''
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "scrapy_spider.middlewares.ScrapySpiderSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "scrapy_spider.middlewares.ScrapySpiderDownloaderMiddleware": 543,
# }
DOWNLOADER_MIDDLEWARES = {
    'xianyu.middlewares.UserAgentDownloaderMiddleware': 543,
}

'''extensions'''
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#     "scrapy_spider.pipelines.ScrapySpiderPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

'''Request 指纹'''
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

'''log'''
# LOG_LEVEL="DEBUG"
# LOG_FILE="data.log"



