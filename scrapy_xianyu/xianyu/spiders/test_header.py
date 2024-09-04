from typing import Any
import scrapy
from scrapy.http import Response
from scrapy import cmdline


class AddHeadersSpider(scrapy.Spider):
    name = 'add_headers'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com']
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        # "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.5,en;q=0.3",
        # "Accept-Encoding": "gzip, deflate",
        # 'Content-Length': '0',
        # "Connection": "keep-alive"
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url,
                                 headers=self.headers,
                                 callback=self.parse)

    def parse(self, response: Response, **kwargs: Any):
        print("---------------------------------------------------------")
        print("response headers: %s" % response.headers)
        print("request headers: %s" % response.request.headers)
        print("---------------------------------------------------------")
        print(response.text)


if __name__ == '__main__':
    cmdline.execute('scrapy crawl add_headers'.split())
