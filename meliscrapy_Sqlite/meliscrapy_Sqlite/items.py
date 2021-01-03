# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MeliscrapySqliteItem(scrapy.Item):

        descripcion = scrapy.Field()
        titulo = scrapy.Field()
        precio = scrapy.Field()
        rooms = scrapy.Field()
        baths = scrapy.Field()
