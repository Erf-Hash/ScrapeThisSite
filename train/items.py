# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class TeamItem(Item):
    name = Field()
    year = Field()
    wins = Field()
    losses = Field()
    ot_losses = Field()
    win_percentage = Field()
    goals_for = Field()
    goals_against = Field()
