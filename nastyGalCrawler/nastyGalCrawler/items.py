import scrapy
from scrapy_djangoitem import DjangoItem
from products.models import NastyGalModel


class NastygalcrawlerItem(DjangoItem):
    django_model = NastyGalModel
    title = scrapy.Field()
    original_price = scrapy.Field()
    sale_price = scrapy.Field()
