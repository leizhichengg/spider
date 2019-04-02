import scrapy
from tutorial.items import TutorialItem
from scrapy_redis.spiders import RedisSpider

class QuotesSpider(RedisSpider):
    name = "quotes"

    redis_key = 'myspider:start_urls'
    
    # start_urls = [
    #         'http://quotes.toscrape.com/page/1',
    #     ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall()
            }
        for a in response.css('li.next a'):
            yield response.follow(a, callback=self.parse)