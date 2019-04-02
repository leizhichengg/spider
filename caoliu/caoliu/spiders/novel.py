import scrapy

class Novel(scrapy.Spider):
    name = 'caoliu_novel'

    start_urls = [
        'http://t66y.com/htm_data/20/1904/3482740.html',
        'http://t66y.com/htm_data/20/1904/3482415.html',
        
    ]

    def parse(self, response):
        # for item in response.xpath('//ul[@class="subject-list"]/li'):
        #     yield {
        #         'title': item.xpath('.//div[@class="info"]/h2/a/@title').get(),
        #         'image': item.xpath('.//div[@class="pic"]/a/img/@src').get(),
        #         'link': item.xpath('.//div[@class="pic"]/a/@href').get(),
        #         'info': item.xpath('.//div[@class="pub"]/text()').get().strip(),
        #         'score': item.xpath('.//div[@class="star clearfix"]/span[2]/text()').get(),
        #     }
        yield {
            'title': response.xpath('//tr[@height="100%"]/td/h4/text()').get(),
            'content': response.xpath('//div[@class="tpc_content do_not_catch"]/text()').getall(),
        }