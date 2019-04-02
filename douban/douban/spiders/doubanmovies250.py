import scrapy
from douban.items import DoubanMovies250Item

class DoubanMovies250(scrapy.Spider):
    name = 'douban_movies_250'
    
    start_urls = [
        'https://movie.douban.com/top250',
    ]

    def parse(self, response):
        for selector in response.xpath('//ol/li'):
            item = DoubanMovies250Item()
            item['index'] = selector.xpath('.//div[@class="pic"]/em/text()').get()
            item['title'] = selector.xpath('.//div[@class="info"]/div/a/span[@class="title"]/text()').get()
            item['image'] = selector.xpath('.//div[@class="pic"]/a/img/@src').get()
            item['link'] = selector.xpath('.//div[@class="pic"]/a/@href').get()
            item['releasetime'] = selector.xpath('.//div[@class="info"]/div[@class="bd"]/p').re(r'.*?(\d{4})')[0]
            item['score'] = selector.xpath('.//div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[2]/text()').get()
            yield item

        for a in response.xpath('.//span[@class="next"]/a/@href'):
            yield response.follow(a, callback=self.parse)