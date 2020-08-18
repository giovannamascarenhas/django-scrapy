from itemadapter import ItemAdapter
from products.models import NastyGalModel


class NastygalcrawlerPipeline(object):
    def process_item(self, item, spider):
        item.save()
        return item
