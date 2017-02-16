#Notes only works with Homes Norfolk right now
#Receives a home property listing uri and returns the images

import scrapy

uri_param = "property/3611-bell-st-norfolk-va-23513/id-400028631997/"

class HomeSpider(scrapy.Spider):
    name = 'homespider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        for title in response.css('h2.entry-title'):
            yield {'title': title.css('a ::text').extract_first()}

        next_page = response.css('div.prev-post > a ::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)