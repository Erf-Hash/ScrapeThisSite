# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class OscarItem(Item):
    title = Field()
    year = Field()
    awards = Field()
    nominations = Field()
    best_picture = Field()

