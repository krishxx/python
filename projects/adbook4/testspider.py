import scrapy
import urllib2

'''
class MySpider(scrapy.Spider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = [
        'http://www.example.com/1.html',
        'http://www.example.com/2.html',
        'http://www.example.com/3.html',
    ]
'''

def parse(self, response):
	print response.xpath('//a/@href').extract()
	for url in response.xpath('//a/@href').extract():
		print url
		yield scrapy.Request(url, callback=self.parse)
		

#parse("www.libero.it", "http://liberomail.libero.it")
import urllib2

website = "WEBSITE"
openwebsite = urllib2.urlopen(website)
html = getwebsite.read()

print html