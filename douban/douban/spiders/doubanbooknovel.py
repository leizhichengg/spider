import scrapy

class DoubanBook(scrapy.Spider):
    name = 'douban_books_novel'
    
    start_urls = [
        'https://book.douban.com/tag/小说',
    ]

    def parse(self, response):
        for item in response.xpath('//ul[@class="subject-list"]/li'):
            yield {
                # 'index': index,
                'title': item.xpath('.//div[@class="info"]/h2/a/@title').get(),
                'image': item.xpath('.//div[@class="pic"]/a/img/@src').get(),
                'link': item.xpath('.//div[@class="pic"]/a/@href').get(),
                'info': item.xpath('.//div[@class="pub"]/text()').get().strip(),
                'score': item.xpath('.//div[@class="star clearfix"]/span[2]/text()').get(),
            }

        for a in response.xpath('.//span[@class="next"]/a/@href'):
            yield response.follow(a, callback=self.parse)