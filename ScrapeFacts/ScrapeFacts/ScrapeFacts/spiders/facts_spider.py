import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import ScrapefactsItem

class FactsSpider(scrapy.Spider):

    name = "facts"
    start_urls = ['https://www.thefactsite.com/1000-interesting-facts/']
    item = ScrapefactsItem()

    def parse(self, response):
        paragraphs = response.css('p')

        for paragraph in paragraphs:
            fact = paragraph.css('.list::text').extract()
            if fact:
                yield {'fact': fact}

        next_page = response.css('.w-full a::attr(href)').get()
        
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url = next_page_url, callback = self.parse)