# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from .items import *
from scrapy.utils.project import get_project_settings
import redis



class XianyuSpiderPipeline:
    def process_item(self, item, spider):
        return item



class ScrapySpiderPipeline:
    def open_spider(self, spider):
        # 初始化db客户端
        host = spider.settings['MONGODB_HOST']
        port = spider.settings['MONGODB_PORT']
        db_name = spider.settings['MONGODB_DBNAME']
        self.client = pymongo.MongoClient(host=host, port=port)
        self.db = self.client[db_name]
        self.collection = self.db[spider.settings['MONGODB_DOCNAME']]
        self.item_list = []

    def process_item(self, item, spider):
        # print('111',type(item))
        # print(ScrapySpiderItem)
        if ScrapySpiderItem == type(item):
            self.item_list.append(dict(item))
        return item

    def close_spider(self, spider):
        # 结束并写入
        self.collection.insert_many(self.item_list)
        print('{}条数据已存入数据库'.format(len(self.item_list)))
        self.client.close()
        print('数据库已关闭')


class ProjectPipeline:
    def open_spider(self, spider):
        # 初始化db客户端
        host = spider.settings['MONGODB_HOST']
        port = spider.settings['MONGODB_PORT']
        db_name = spider.settings['MONGODB_DBNAME']
        self.client = pymongo.MongoClient(host=host, port=port)
        self.db = self.client[db_name]
        self.collection = self.db[spider.settings['MONGODB_DOCNAME2']]
        self.item_list = []

    def process_item(self, item, spider):
        # print('adsfa',type(item))
        # print(ProjectItem)
        if ProjectItem == type(item):
            self.item_list.append(dict(item))
        return item

    def close_spider(self, spider):
        # 结束并写入
        self.collection.insert_many(self.item_list)
        print('{}条数据已存入数据库'.format(len(self.item_list)))
        self.client.close()
        print('数据库已关闭')


# class RedisPipeline:
#     def open_spider(self, spider):
#         host = spider.settings['MONGODB_HOST']
#         port = spider.settings['MONGODB_PORT']
#         db_name = spider.settings['MONGODB_DBNAME']
#         self.client = pymongo.MongoClient(host=host, port=port)
#         self.db = self.client[db_name]
#         self.collection = self.db[spider.settings['MONGODB_DOCNAME']]
#         self.item_list = []
#
#     def process_item(self, item, spider):
#         self.item_list.append(dict(item))
#         return item
#
#     def close_spider(self, spider):
#         self.collection.insert_many(self.item_list)
#         print('{}条数据已存入数据库'.format(len(self.item_list)))
#         self.client.close()
#         print('数据库已关闭')
#
#
# class NewsSpiderPipeline:
#     def process_item(self, item, spider):
#         host = 'localhost'
#         port = 27017
#         db_name = 'spider'
#         client = pymongo.MongoClient(host=host, port=port)
#         db = client[db_name]
#         collection = db['eastmoney_news']
#         collection.insert_one(dict(item))
#         return item


