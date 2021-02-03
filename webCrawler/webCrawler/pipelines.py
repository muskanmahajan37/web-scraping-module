# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2
from decouple import config
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WebcrawlerPipeline:
    def open_spider(self, spider):
        username = config('DB_USER_1')
        password = config('BD_PASS_1')
        database = config('DB_NAME')
        port = config('DB_PORT')
        hostname = config('DB_HOST')
        self.connection = psycopg2.connect(user=username,
                                           password=password,
                                           port=port,
                                           database=database,
                                           host=hostname)
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        return item

    def close_item(self, spider):
        self.cursor.close()
        self.connection.close()
