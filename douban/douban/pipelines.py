# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class DoubanPipeline(object):
    def process_item(self, item, spider):
        return item

class DoubanMovies250Pipeline(object):
    def open_spider(self, spider):
        self.file = open('douban_movies_250.json', 'w')
    
    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        output = json.dumps(item, indent=4, separators=(',', ': '), ensure_ascii=False)
        self.file.write(output)
        return item

class DoubanBookNovelPipeline(object):
    def open_spider(self, spider):
        self.file = open('douban_books_novel.json', 'w')
    
    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        output = json.dumps(item, indent=4, separators=(',', ': '), ensure_ascii=False)
        self.file.write(output)
        return item

class DoubanBookAllPipeline(object):
    def open_spider(self, spider):
        self.file = open('douban_books_alll.json', 'w')
    
    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        output = json.dumps(item, indent=4, separators=(',', ': '), ensure_ascii=False)
        self.file.write(output)
        return item