from django.db import models


class Product(models.Model):
    product_id = models.TextField()
    name = models.TextField()
    brand = models.TextField()
    categories = models.TextField()
    description = models.TextField()
    material = models.TextField()
    made_in = models.TextField()
    url = models.URLField()
    site = models.URLField()

    def __str__(self):
        return self.name


class Image(models.Model):
    url = models.URLField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

# class Price(models.Model):
#     product_id = models.ForeignKey(Product)
#     price = models.DecimalField()
#     color = models.CharField()
#     size = models.CharField()
#     stock_level = models.CharField()
#     currency = models.CharField()
#     date = models.DateTimeField()
