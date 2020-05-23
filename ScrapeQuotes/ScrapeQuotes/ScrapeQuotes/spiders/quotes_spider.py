import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import ScrapequotesItem

class QuotesSpider(scrapy.Spider):

    name = "quotes"
    start_urls = ['https://www.azquotes.com/top_quotes.html']
    item = ScrapequotesItem()
    counter = 0

    def parse(self, response):
        all_quotes = response.css('.wrap-block')

        for quote in all_quotes:
            QuotesSpider.item['quote'] = quote.css('.title::text').get()
            QuotesSpider.item['author'] = quote.css('.author a::text').get()
            QuotesSpider.counter += 1
            yield {QuotesSpider.counter: QuotesSpider.item}

        next_page = response.css('li.next a::attr(href)').get()
        
        if next_page:
            next_page_url = 'https://www.azquotes.com/' + next_page
            yield scrapy.Request(url = next_page_url, callback = self.parse)