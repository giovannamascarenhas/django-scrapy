import scrapy
from nastyGalCrawler.items import NastygalcrawlerItem


class NastyGalSpider(scrapy.Spider):
    name = "nasty-gal"
    start_urls = ["https://www.nastygal.com/eu/whats-new?promo_bottomstrip_1_whats-new"]

    def parse(self, response):
        products = response.css('.product-tile')
        for product in products:
            item = NastygalcrawlerItem()
            item["title"] = product.css('.product-tile-name a::text').get().split('\n')[1]
            item["original_price"] = product.css('span.product-standard-price::text').get().split('\n')[1]
            item["sale_price"] = product.css('span.product-sales-price::text').get().split('\n')[1]
            yield item
         