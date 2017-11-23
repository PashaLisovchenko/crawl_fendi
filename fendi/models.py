from django.db import models


class Categories(models.Model):
    name = models.CharField()


class Images(models.Model):
    pass


class Product(models.Model):
    product = models.CharField()
    name = models.CharField()
    brand = models.CharField()
    description = models.CharField()
    made_in = models.CharField()
    categories = models.ForeignKey(Categories)
    materials = models.CharField()
    # image = models.()
    url = models.CharField()
    site = models.CharField()


class Price(models.Model):
    product_id = models.ForeignKey(Product)
    price = models.DecimalField()
    color = models.CharField()
    size = models.CharField()
    stock_level = models.CharField()
    currency = models.CharField()
    date = models.DateTimeField()
