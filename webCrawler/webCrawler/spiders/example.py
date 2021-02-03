import scrapy
from scrapy.loader import ItemLoader
from ..items import Clothing


class SupComSpider(scrapy.Spider):
    name = 'SupCom'

    def start_requests(self):
        urls = [
            'https://www.supremecommunity.com/season/latest/droplists/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.xpath(
            '//div[contains(@class,"col-sm-4 col-xs-12 app-lr-pad-2")][contains(@id,"box-latest")]/a/@href').get()
        if page is not None:
            yield scrapy.Request('https://www.supremecommunity.com' + page, callback=self.id_parser)
            # response.css('.menu-horizontal>* a::attr(href)').getall() #css
            # response.xpath('//ul[contains(@class,"menu-horizontal")]/li/a/@href').getall() #xPath
            # page = response.xpath('//div[contains(@class,"col-sm-4 col-xs-12 app-lr-pad-2")][contains(@id,"box-latest")]/a/@href').get()
            # page = response.css('div#box-latest>a').attrib['href']
        # else:
        #     item_ids = response.xpath("//div[@class='card-details']/@data-itemid").getall()
        #     if item_ids is not None:
        #         for item_id in item_ids:
        #             yield scrapy.Request(f'https://www.supremecommunity.com/season/itemdetails/{item_id}/mobile/',
        #                                  callback=self.items_parser)

    def id_parser(self, response):
        item_ids = response.xpath("//div[@class='card-details']/@data-itemid").getall()
        if item_ids is not None:
            for item_id in item_ids:
                yield scrapy.Request(f'https://www.supremecommunity.com/season/itemdetails/{item_id}/mobile/',
                                     callback=self.item_parser)

    def item_parser(self, response):
        loader = ItemLoader(item=Clothing(), response=response)
        loader.add_xpath('name', './/div[@class="card-details"]/@data-itemname')
        loader.add_xpath('price', './/div[@class="itemdetails-centered itemdetails-labels"]')
        loader.add_xpath('image_url', './/img[@id="detailImage"]/@src')
        loader.add_xpath('color', './/img[@id="detailImage"]/@src')
        #
        # price = piece.xpath('normalize-space(.//span/text())').get()
        # if price is not None:
        #     sup_item['price'] = price[1:price.find('/')]
        # else:
        #     sup_item['price'] = price
        # sup_item['image_url'] = 'https://www.supremecommunity.com' + piece.xpath('.//img/@src').get()
        # sup_item['currency'] = 'Sup'
        yield loader.load_item()


'''
for item in item_names:
...     name = item.xpath('./text()').get()
...     print(name)


response.xpath("//div[@class='card-details']/@data-itemid").getall()
'''
