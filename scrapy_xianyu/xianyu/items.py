# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapySpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    type = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
    link = scrapy.Field()
    tags = scrapy.Field()
    relasetime = scrapy.Field()



class ProjectItem(scrapy.Item):
    type = scrapy.Field()
    tag = scrapy.Field()
    link = scrapy.Field()
