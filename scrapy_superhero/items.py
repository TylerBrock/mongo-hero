# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class SuperHeroItem(Item):
	name = Field()
	aliases = Field()
	biography = Field()
	appearance = Field()
	work = Field()
	relations = Field()

