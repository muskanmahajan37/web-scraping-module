# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class Clothing(scrapy.Item):
    name = scrapy.Field(
        output_processor=TakeFirst()
    )
    category = scrapy.Field(
        output_processor=TakeFirst()
    )
    image_url = scrapy.Field(
        output_processor=TakeFirst()
    )
    price = scrapy.Field(
        output_processor=TakeFirst()
    )
    colors = scrapy.Field(
        output_processor=TakeFirst()
    )


class WebcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
