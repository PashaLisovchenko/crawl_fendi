from celery.task import task
from .models import Product, Image


@task(name='add_product')
def add_product(item_list):
    for item in item_list:
        product, created = Product.objects.get_or_create(
            product_id=item.get('id'),
            name=item.get('name'),
            brand=item.get('brand'),
            categories=item.get('categories'),
            description=item.get('description'),
            material=item.get('materials'),
            made_in=item.get('made_in'),
            url=item.get('url'),
            site=item.get('site')
        )
        print(product, created)
        if created:
            for url in item.get('images', []):
                Image.objects.get_or_create(
                    url=url,
                    product=product
                )
