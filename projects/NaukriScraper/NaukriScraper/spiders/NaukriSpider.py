import scrapy
#from NaukriScraper.items import NaukriItem

class NaukriSpider(scrapy.Spider):
	name = "naukri"
	start_urls = [
		"https://www.naukri.com/jobs-in-hyderabad-secunderabad"
	]
	
	def parse(self, response):
		for selector in response.xpath("//li[@itemprop='title']"):
			item = NaukriItem()
			#item["title"] = selector.xpath("itle=
			item["location"] = selector.xpath("span[@itemprop='jobLocation']text()").extract()
			item["company"] = selector.xpath("span[@itemprop='hiringOrganization']text()").extract()
			yield item