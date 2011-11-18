from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from scrapy_superhero.items import SuperHeroItem

BASE_URL = "http://www.superherodb.com"

class SuperHeroSpider(BaseSpider):
	name = "index"
	allowed_domains = [ "superherodb.com" ]
	start_urls = [
		"http://www.superherodb.com/characters/"
	]
	
	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		hero_urls = hxs.select('//div[@class="contentCol3"]//li/a/@href').extract()
		return (
			Request(
				BASE_URL + hero_url,
				callback=self.parse_hero
			) for hero_url in hero_urls
		)
		
	def parse_hero(self, response):
		hxs = HtmlXPathSelector(response)
		item = SuperHeroItem()
		item['name'] = hxs.select('//div[@class="titleHolder"]//h1/text()').extract()
		headers = hxs.select('//div[@id="tab1c"]//div[@class="contentColLeft"]//h4')
		sections = hxs.select('//div[@id="tab1c"]//div[@class="contentColLeft"]//div[@class="tableHolder"]')
		
		for index, section in enumerate(sections):
			name = "biography" if index == 0 else headers.select('text()').extract()[index-1]
			data = {}
			attributes = section.select('./div[@class="tableRow"]')
			
			for i, row in enumerate(attributes):
				attribute = row.select('//div[@class="tableCaption"]')[i].select('text()').extract()[0]
				vals = row.select('//div[@class="tableData"]')[i].select('text()').extract()
				data[attribute] = [(' ').join(val.split()) for val in vals]
			
			item[name.lower()] = data
			yield item