import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class JokesSpider(scrapy.Spider):

    name = "jokes"
    start_urls = ['https://onelinefun.com/time/']

    def parse(self, response):
        all_jokes = response.css('.o')
        counter = 0

        for j in all_jokes:
            joke = j.css('p::text').get()
            counter += 1
            yield {counter: joke}