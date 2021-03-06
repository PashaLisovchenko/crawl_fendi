import scrapy
import datetime
from ..items import Product, Price
from scrapy_redis.spiders import RedisSpider

SITE = "https://www.fendi.com"


class FendiSpider(RedisSpider):
    name = 'fendi'

    def __init__(self, url=None, *args, **kwargs):
        super(FendiSpider, self).__init__(*args, **kwargs)
        self.url = url

    def parse(self, response):
        if 'man' in response.url.split('/'):
            category_href = response.xpath("//div[@id='man-popover']/div[@class='subcategories']"
                                           "/div[contains(@class, 'two-cols')]/div[contains(@class, 'exp')]"
                                           "/ul[contains(@class, 'expandable-xs')]/li[contains(@class, ' ')]"
                                           "/a/@href").extract()

            category_full_url = [SITE+href for href in category_href][0:-1]
            # print(category_full_url)
            for url in category_full_url:
                yield scrapy.Request(url=url, callback=self.parse_item)
        elif 'woman' in response.url.split('/'):
            category_href = response.xpath("//div[@id='woman-popover']/div[@class='subcategories']"
                                           "/div[contains(@class, 'two-cols')]/div[contains(@class, 'exp')]"
                                           "/ul[contains(@class, 'expandable-xs')]/li[contains(@class, ' ')]"
                                           "/a/@href").extract()

            category_full_url = [SITE + href for href in category_href][0:-1]
            # print(category_full_url)
            for url in category_full_url:
                yield scrapy.Request(url=url, callback=self.parse_item)

    def parse_item(self, response):
        item_href = response.xpath('//div[contains(@class,"product-card")]/div[@class="inner"]/figure'
                                   '/a/@href').extract()
        item_full_url = [SITE + href for href in item_href]
        for url in item_full_url:
            yield scrapy.Request(url=url, callback=self.parse_detail, dont_filter=True)

    def parse_detail(self, response):
        product = Product()
        price = Price()
        product['id'] = response.xpath("//div[@class='product-info']/div[@class='product-description']/p[@class='code']"
                                       "/span/text()").extract_first()
        product['name'] = response.xpath("//div[@class='product-info']/div[@class='product-description']/h1"
                                         "/text()").extract_first()
        product['brand'] = 'Fendi'
        product['description'] = ''.join(response.xpath("//div[@class='tab-content']/div[contains(@class, 'tab-pane')]"
                                                        "/p/text()").extract())
        made_in = response.xpath("//div[@class='tab-content']/div[contains(@class, 'tab-pane')]/p"
                                 "/text()").extract()
        if len(made_in) > 1:
            product['made_in'] = made_in[1].strip()
        else:
            product['made_in'] = 'Made in Italy'

        product['categories'] = ','.join([response.xpath("//div[@class='breadcrumbs']/section[@class='breadcrumb']"
                                                         "/a[@class='main-area']/text()").extract_first(''),
                                         response.xpath("//div[@class='breadcrumbs']/section[@class='breadcrumb']"
                                                        "/div[@class='dropdown']/button[@id='dropdown-main-category']"
                                                        "/text()").extract_first()
                                          ])
        materials = response.xpath("//div[@class='tab-content']/div[contains(@class, 'tab-pane')]/ul/li[2]"
                                   "/span/text()").extract_first()
        if materials:
            product['materials'] = materials
        else:
            product['materials'] = ''

        product['images'] = response.xpath("//div[contains(@class, 'carousel-nav')]/div"
                                           "/img/@data-src").extract()
        product['url'] = response.url
        product['site'] = SITE

        yield product

        # price['product_id'] = response.xpath("//div[@class='product-info']/div[@class='product-description']"
        #                                      "/p[@class='code']/span/text()").extract_first()
        # price_params = dict()
        #
        # price_params['price'] = response.xpath("//div[@class='product-info']/div[@class='product-description']"
        #                                        "/div[contains(@class, 'prices')]/span[@class='price ']"
        #                                        "/text()").extract_first('').strip()
        # price_params['color'] = response.xpath("//div[@class='product-variant']/a/img/@alt").extract()
        #
        # price_params['size'] = [size.replace('\n', '').strip()
        #                         for size in response.xpath("//div[@class='form-group']/select"
        #                                                    "/option[@data-sold-out='false']//text()").extract()]
        # price['params'] = price_params
        # stock = response.xpath("//div[contains(@class,'product-form')]/form/span[@class='message']/text()")
        # if stock:
        #     price['stock_level'] = stock.extract_first('').strip()
        # else:
        #     price['stock_level'] = 'Available'
        # price['currency'] = 'USD'
        # price['date'] = str(datetime.datetime.now())
        #
        # yield price
