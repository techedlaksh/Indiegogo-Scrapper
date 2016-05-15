from scrapy.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector
from indiegogo.items import IndiegogoItem
from scrapy.http import Request

class MySpider(BaseSpider):
	name = "indiegogo"
	allowed_domains = ["indiegogo.com"]
	start_urls = ["http://www.indiegogo.com/explore/technology",]

	def parse(self,response):
		hxs = HtmlXPathSelector(response)
		titles = hxs.select('//*[contains(@class, "discoveryCard-title")]/text()').extract()
		for title in titles:
			item = IndiegogoItem()
			item["title"] = title
			yield item