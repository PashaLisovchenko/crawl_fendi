from fendi.tasks import add_product
from .items import Product


class ScrapyFendiPipeline(object):

    def __init__(self):
        self.product_packet = list()

    def save_items(self):
        add_product.delay(
            [dict(product) for product in self.product_packet]
        )
        self.product_packet.clear()

    def process_item(self, item, spider):
        if isinstance(item, Product):
            self.product_packet.append(item)
        # if len(self.product_packet) > 50:
        self.save_items()
        return item

    def close_spider(self, spider):
        self.product_packet and self.save_items()
