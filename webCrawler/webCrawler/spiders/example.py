import scrapy


class SupComSpider(scrapy.Spider):
    name = 'SupCom'

    def start_requests(self):
        urls = [
            'https://www.supremecommunity.com/season/latest/droplists/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.xpath('//div[contains(@class,"col-sm-4 col-xs-12 app-lr-pad-2")][contains(@id,"box-latest")]/a/@href').get()
        if page is not None:
            yield scrapy.Request('https://www.supremecommunity.com/'+page, callback=self.parse)
            # response.css('.menu-horizontal>* a::attr(href)').getall() #css
            # response.xpath('//ul[contains(@class,"menu-horizontal")]/li/a/@href').getall() #xPath
            # page = response.xpath('//div[contains(@class,"col-sm-4 col-xs-12 app-lr-pad-2")][contains(@id,"box-latest")]/a/@href').get()
            # page = response.css('div#box-latest>a').attrib['href']
        else:
            print("Done.")