# -*- coding: utf-8 -*-
from pymongo import MongoClient

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class sgOffTheTee(object):
    collection = 'sgOffTheTee'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        #self.db[self.collection].create_index("name",unique=True)

    def close_spider(self,spider):
        self.client.close()
    

    def process_item(self, item, spider):
       # if spider.name ==  'sgOffTheTee':
        #    collection=spider.name
        self.db[self.collection].insert_one(dict(item))
        return item

class rbgHeritage(object):
    collection = 'rbgHeritage'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        #self.db[self.collection].create_index("name",unique=True)

    def close_spider(self,spider):
        self.client.close()
    

    def process_item(self, item, spider):
        # if spider.name ==  'rbgHeritage':
        #     collection=spider.name
        self.db[self.collection].insert_one(dict(item))
        return item

class wellsFargo(object):
    collection = 'wellsFargo'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        #self.db[self.collection].create_index("name",unique=True)

    def close_spider(self,spider):
        self.client.close()
    

    def process_item(self, item, spider):
        # if spider.name ==  'rbgHeritage':
        #     collection=spider.name
        self.db[self.collection].insert_one(dict(item))
        return item

class rbgHeritagePlayer(object):
    collection = 'rbgHeritagePlayer'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        #self.db[self.collection].create_index("name",unique=True)

    def close_spider(self,spider):
        self.client.close()
    

    def process_item(self, item, spider):
        # if spider.name ==  'rbgHeritagePlayer':
        #     collection=spider.name
        self.db[self.collection].insert_one(dict(item))
        return item

class expanded(object):
    collection = 'expanded'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        #self.db[self.collection].create_index("name",unique=True)

    def close_spider(self,spider):
        self.client.close()
    

    def process_item(self, item, spider):
        # if spider.name ==  'rbgHeritagePlayer':
        #     collection=spider.name
        self.db[self.collection].insert_one(dict(item))
        return item

class expanded2(object):
    collection = 'expanded2'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        #self.db[self.collection].create_index("name",unique=True)

    def close_spider(self,spider):
        self.client.close()
    

    def process_item(self, item, spider):
        # if spider.name ==  'rbgHeritagePlayer':
        #     collection=spider.name
        self.db[self.collection].insert_one(dict(item))
        return item