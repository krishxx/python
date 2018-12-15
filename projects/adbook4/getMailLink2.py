import requests
from bs4 import BeautifulSoup
import re
import validators
import urllib2
import urllib

def getMailPageLink2(url):
	page = requests.get(url)
	html_content = page.text
	#print html_content
	soup = BeautifulSoup(html_content, 'lxml')
	links = soup.find_all('a')
	for item in links:
		#print item
		if 'mail' in item:
			print item
			one, two, three = item.split('"',2)
			print two 
	
        try:
                #page = request.get(url)
		#html_content = page.text
		#soup = BeautifulSoup(html_content, lxml)
		#links = []
		#links = soup.find_all('a')
		#print links 
                '''
		soup = BeautifulSoup(page.read(), 'html')
		print soup
                for a in soup.find_all("a", text=re.compile('mail')):
			print a['href']
                        return a['href']
                for a in soup.find_all("a", text=re.compile('login')):
			print a['href']
                        return a['href']
                for a in soup.find_all("a", text=re.compile('account')):
			print a['href']
                        return a['href']
		'''
                #page.close()
        except:
                print 'exception: '+url
        return None

getMailPageLink2('https://in.yahoo.com/?p=us')
