# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CaoliuPipeline(object):

    def close_spider(self, spider):
        self.file.close()    

    def process_item(self, item, spider):
        self.file = open(item['title'] + '.txt', 'w', encoding='utf-8')
        content = item['content']
        for para in content:
            self.file.write(para + '\n')
        return item