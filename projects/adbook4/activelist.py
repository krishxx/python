import re
import sys
import validators
import urllib2
import scrapy
import httplib
import time
from time import gmtime, strftime

print "*****HELLO ADDRESSBOOK*********"
print "***TIME: "+strftime("%Y-%m-%d %H:%M:%S***", gmtime())
print "*******************************"

def getRedirectedLink(url):
	newUrl = url
	h = httplib.HTTPConnection(url)	
	try:
		h.request('HEAD', '/')
		response = h.getresponse()
		#Check for 30x status code
		if 300 <= response.status < 400:
			#It's a redirect
			newUrl = response.getheader('Location')			
			print 'newUrl: '+newUrl
	except:
		newUrl = None
		print "exception in getRedirectLink due to "+url		
	h.close()
	return newUrl
		
def parse_urlfile(ipfile, opfile):
	fin = open(ipfile, "r")
	fout = open(opfile, "w")
	fout2 = open('mailUrls.txt', "w")
	#lines = fin.readlines()
	for line in fin:
		url = line.split()
		print url[0]
		fout2.write('http://www.mail.'+url[0]+'\n');
		fout2.write('https://www.mail.'+url[0]+'\n');
		fout2.write('http://www.webmail.'+url[0]+'\n');
		fout2.write('https://www.webmail.'+url[0]+'\n');
		fout2.write('mail.'+url[0]+'\n');
		fout2.write('https://connect.'+url[0]+'\n');
		if(validators.url('https://www.'+url[0])):			
			newUrl = getRedirectedLink(url[0])
			if newUrl is not None:
				fout.write(newUrl+'\n')
		#else:
		#	fout.write("Not valid "+url[0]+'\n')
	fin.close()
	fout.close()
	fout2.close()
	return
	
def listOutMailLinks(ipfile, opfile):
	fin = open(ipfile, "r")
	fout = open(opfile, "w")
	for line in fin:
		if('webmail' in line):
			try:
				fp = urllib2.urlopen(line)
				if fp is not None:
					fout.write(line)
				fp.close()
			except:
				print 'exception with '+line
		elif('http://www' in line):
			start, end = line.split('www')
			url2 = start+'www.mail'+end
			try:
				fp = urllib2.urlopen(url2)
				if fp is not None:
					fout.write(url2)
				fp.close()
			except:
				print 'exception with '+url2
		elif('https://www' in line):
			start, end = line.split('www')
			url2 = start+'www.mail'+end
			try:
				fp = urllib2.urlopen(url2)
				if fp is not None:
					fout.write(url2)
				fp.close()
			except:
				print 'exception with '+url2
		elif(('http' in line) and not('www' in line)):		
			start, end = line.split('//')
			url2 = start+'//www.mail.'+end
			try:
				fp = urllib2.urlopen(url2)
				if fp is not None:
					fout.write(url2)
				fp.close()
			except:
				print 'exception wth '+url2
		elif(not('http://www' in line) or not('https://www' in line) or not('www' in line)):
			try:
				url2 = 'mail.'+line
				fp = urllib2.urlopen(url2)
				if fp is not None:
					fout.write(url2)
				fp.close()
			except:
				print 'exception with '+url2		
			try:
				url2 = 'http://www.mail.'+line
				fp = urllib2.urlopen(url2)
				if fp is not None:
					fout.write(url2)
				fp.close()
			except:
				print 'exception with '+url2			
			try:			
				url2 = 'https://www.mail.'+line
				fp = urllib2.urlopen(url2)
				if fp is not None:
					fout.write(url2)
				fp.close()
			except:
				print 'exception with '+url2			
			try:
				url2 = 'www.mail.'+line
				fp = urllib2.urlopen(url2)				
				if fp is not None:
					fout.write(url2)
				fp.close()
			except:
				print 'exception with '+url2
	fin.close()
	fout.close()
	return

def validateMailLinks(ipfile, opfile):
	fin = open(ipfile, "r")
	fout = open(opfile, "w")
	for line in fin:
		try:
			mxfp = urllib2.urlopen(line)				
			if mxfp is not None:
				fout.write(line+'\n')
				mxlfp.close()
				continue
		except:
			print "exception with "+line
			mxfp.close()
	fin.close()
	fout.close()
	return
	
def list_out_mx(ipfile, opfile):
	fin = open(ipfile, "r")
	fout = open(opfile, "w")
	for line in fin:
		if('webmail' in line):
			print 'webmail:'+line
			if not('http' in line):
				url = 'https://'+line
			else:
				url = line
		elif('www' in line):
			start, end = line.split('www')
			print 'end part: '+end
			url = 'https://www.mail'+end		
		#elif not ('http://www' in line):			
		#	url = 'https://www.mail.'+line			
		#elif ('http://www' in line):
		#	start, end = line.split('//www')
		#	url = start+'//www.mail.'+end			
		try:
			#url = "http://www.mail."+line			
			mxfp = urllib2.urlopen(url)				
			if mxfp is not None:
				fout.write(url+'\n')
				mxfp.close()
				continue
		except:
			print "exception with "+url
	fin.close()
	fout.close()
	return
'''
//copied from above
if mxfp is None:
	url = "https://www.mail."+line
	mxfp = urllib2.urlopen(url)
		try:
			if mxfp is None:
				url = "http://www.webmail."+line
				mxfp = urllib2.urlopen(url)
			 else:
				fout.write(url+'\n')
				continue
		except:
			print "exception with www.mail. "+url+" occured"			
			elif mxfp is None:
				url = "http://www.smtp."+line
				mxfp = urllib2.urlopen(url)
			elif mxfp is None:
				url = "http://www.outbound."+line
				mxfp = urllib2.urlopen(url)			
			elif mxfp is None:
				url = "http://www.outgoing."+line
				mxfp = urllib2.urlopen(url)
			elif mxfp is None:
				url = "http://www.smtp.mail."+line
				mxfp = urllib2.urlopen(url)		
			if mxfp is not None:
				fout.write(url+'\n')
				continue
	fin.close()
	fout.close()
	return
def listout_mailserver(ipfile, opfile):
	fin = open(ipfile, "r")
	fout = open(opfile, "w")
	for line in fin:
		url = "https://www."+line;
		#selector.xpath('//a[href=$url]', 
'''
#print time
#print getRedirectedLink("cox.net")
parse_urlfile("raw_domain_list.txt", "active_domain_list.txt")
#list_out_mx("active_domain_list.txt", "mx_list.txt")
listOutMailLinks('active_domain_list.txt', 'mx_list.txt')
validateMailLinks('mailUrls.txt', 'login_page_links.txt')