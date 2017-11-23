from django.db import models


class Product(models.Model):
    pass


class Price(models.Model):
    pass


# class Product(scrapy.Item):
#     id = scrapy.Field()
#     name = scrapy.Field()
#     brand = scrapy.Field()
#     description = scrapy.Field()
#     made_in = scrapy.Field()
#     categories = scrapy.Field()
#     materials = scrapy.Field()
#     images = scrapy.Field()
#     url = scrapy.Field()
#     site = scrapy.Field()
#
#
# class Price(scrapy.Item):
#     product_id = scrapy.Field()
#     params = scrapy.Field()
#     stock_level = scrapy.Field()
#     currency = scrapy.Field()
#     date = scrapy.Field()