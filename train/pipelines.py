# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TrainPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        adapter['name'] = adapter['name'].strip()
        adapter['year'] = int(adapter['year'].strip())
        adapter['wins'] = int(adapter['wins'].strip())
        adapter['losses'] = int(adapter['losses'].strip())
        if adapter['ot_losses']:
            adapter['ot_losses'] = int(adapter['ot_losses'].strip())
        if adapter['win_percentage']:
            adapter['win_percentage'] = float(adapter['win_percentage'].strip())
        adapter['goals_for'] = int(adapter['goals_for'].strip())
        adapter['goals_against'] = int(adapter['goals_against'].strip())

        return item
