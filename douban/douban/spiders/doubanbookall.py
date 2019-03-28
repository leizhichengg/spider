import scrapy

class DoubanBookAll(scrapy.Spider):
    name = 'douban_books_all'

    tag_url = 'https://book.douban.com/tag/?view=cloud'

    tags = [
        '小说', '历史', '日本', '外国文学', '文学', '中国', 
        '心理学', '漫画', '哲学', '随笔', '中国文学', '经典', 
        '推理', '美国', '爱情', '绘本', '日本文学', '传记', 
        '社会学', '文化', '散文', '青春', '科普', '英国', 
        '东野圭吾', '成长', '科幻', '旅行', '生活', '悬疑', 
        '艺术', '言情', '思维', '经济学', '社会', '村上春树', 
        '心理', '管理', '法国', '设计', '励志', '台湾', 
        '政治', '经济', '女性', '人生', '诗歌', '好书，值得一读', 
        '奇幻', '商业', '武侠', '童话', '日本漫画', '摄影', 
        '推理小说', '金融', '英国文学', '建筑', '人性', '美国文学', 
        '宗教', '耽美', '韩寒', '儿童文学', '电影', '古典文学', 
        '名著', '计算机', '互联网', '政治学', '投资', '我想读这本书', 
        '数学', '王小波', '个人管理', '教育', '亦舒', '余华', 
        '杂文', '网络小说', '职场', '三毛', '人类学', '美食', 
        '中国历史', '東野圭吾', '张爱玲', '纪实', '治愈', '香港', 
        '工具书', '回忆录', '科幻小说', '德国', '安妮宝贝', '当代文学', 
        '思想', '阿加莎·克里斯蒂', '编程', '营销', '日系推理', '散文随笔', 
        '温暖', '金庸', '游记', '法国文学', '穿越', '英语', '国学', 
        '教材', '郭敬明', '时间管理', '科学', '心灵', '轻小说', 
        '政治哲学', '英文原版', '刘慈欣', '毛姆', '自我管理']

    start_urls = [
        'https://book.douban.com/tag/小说',
        'https://book.douban.com/tag/历史',
        'https://book.douban.com/tag/日本',
        'https://book.douban.com/tag/外国文学',
        'https://book.douban.com/tag/文学',
        'https://book.douban.com/tag/中国',
        'https://book.douban.com/tag/心理学',
        'https://book.douban.com/tag/漫画',
        'https://book.douban.com/tag/哲学',
        'https://book.douban.com/tag/随笔',
        'https://book.douban.com/tag/中国文学',
        'https://book.douban.com/tag/经典',

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

