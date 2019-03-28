import scrapy

class DoubanMovies250(scrapy.Spider):
    name = 'douban_movies_250'
    
    start_urls = [
        'https://movie.douban.com/top250',
    ]

    def parse(self, response):
        for item in response.xpath('//ol/li'):
            yield {
                'index': item.xpath('.//div[@class="pic"]/em/text()').get(),
                'title': item.xpath('.//div[@class="info"]/div/a/span[@class="title"]/text()').get(),
                'image': item.xpath('.//div[@class="pic"]/a/img/@src').get(),
                'link': item.xpath('.//div[@class="pic"]/a/@href').get(),
                'releasetime': item.xpath('.//div[@class="info"]/div[@class="bd"]/p').re(r'.*?(\d{4})')[0],
                'score': item.xpath('.//div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[2]/text()').get(),
            }

        for a in response.xpath('.//span[@class="next"]/a/@href'):
            yield response.follow(a, callback=self.parse)