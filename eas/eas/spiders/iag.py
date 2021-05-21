import scrapy
from eas.items import EasItem
class PostsSpider(scrapy.Spider):

    name = "iag"
    start_urls = ['https://iag.mn/mn/index.php?pid=70']

    def parse(self, response):
        item = EasItem()
        for post in response.css('div.onens'):
                item['title'] = post.css('h1.bld3::text').get()
                item['date'] = post.css('h1.txt7::text').get()
                item['description'] = post.css('p::text').get()

                yield item
        i = 1
        while i < 5:
            next_page = response.css('td.selected a::attr(href)')[i].get()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
                i += 1
 
    