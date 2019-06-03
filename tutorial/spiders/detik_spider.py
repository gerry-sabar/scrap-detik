import scrapyc

class DetikSpider(scrapy.Spider):
    name = "detik"

    def start_requests(self):
        urls = [
            'https://www.detik.com/mostpopular',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for content in response.xpath('//li'):
            yield {
                'title': content.css('h5::text').get(),
                'link': content.css('a::attr(href)').get(),
            }
