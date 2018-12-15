#!/usr/bin/python
import re
import sys
import validators
import urllib2
import scrapy
import httplib
import time
from time import gmtime, strftime
import thread
from itertools import izip_longest
import glob, os
import glob2
from bs4 import BeautifulSoup

print "*****HELLO ADDRESSBOOK*********"
print "***TIME: "+strftime("%Y-%m-%d %H:%M:%S***", gmtime())
print "*******************************"

def grouper(n, iterable, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

entries = 50000 #no.of entries can be changed
totFiles = 0

print "removing existing split files"
filelist = glob.glob("split_file*.txt")
for f in filelist:
	os.remove(f)
	
with open('raw_domain_list.txt') as f:
    for i, g in enumerate(grouper(entries, f, fillvalue=''), 1):
        with open('split_file_{0}.txt'.format(i * entries), 'w') as fout:
            fout.writelines(g)
	totFiles = i

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

def getMailPageLink(url):
	mlurllist = ['https://www.mail.'+url, 'http://www.mail.'+url, 'http://www.webmail.'+url, 'mailpec.'+url, 'vanitymail.'+url, 'registration.'+url,'https://www.webmail.'+url, url+'/mail', 'mail.'+url, 'account.'+url]	
	for item in mlurllist:
		try:
			mxfp = urllib2.urlopen(item)
			if mxfp is not None:
				#print item
				mxfp.close()
				return item				
		except:
			continue
			#do nothing
	return None
def getRegSetupLink(url):
        reglist = ['https://www.register.'+url, 'http://www.register.'+url, 'http://www.account.'+url, 'https://www.registrierung.'+url, 'http://registrazione.'+url, 'http://www.'+url+'/subscribe', 'http://www.'+url+'/registro', 'https://www.'+url+'/registro', 'https://www.subscribe.'+url]
        for item in reglist:
                try:
                        regfp = urllib2.urlopen(item)
                        if regfp is not None:
                                print item
                                regfp.close()
                                return item
                except:
                        continue
                        #do nothing
        return None

def getMailPageLink2(url):
	try:
		page = urllib2.urlopen(url)
		soup = BeautifulSoup(page.read())
		for a in soup.find_all("a", text=re.compile('mail')):
			return a['href']
		for a in soup.find_all("a", text=re.compile('login')):
			return a['href']
		for a in soup.find_all("a", text=re.compile('account')):
			return a['href']
		page.close()
	except:
		print 'exception: '+url
	return None	
# Define a function for the thread
def process_urls(threadName, ipfile):	
	print 'NAME :' + threadName +' FILE :'+ ipfile
	fin = open(ipfile, "r")
	one, two = ipfile.split('.')
	opfile = one+'_mxout.'+two
	opfile2 = one+'_regout.'+two
	fout = open(opfile, "w")
	fout2 = open(opfile2, "w")
	for line in fin:
		url = line.split()
		if(validators.url('https://www.'+url[0])):
			mailPg = getMailPageLink(url[0])
			if mailPg is not None:
				fout.write(mailPg+'\n')	
				regPg = getRegSetupLink(url[0])
				if regPg is not None:
					fout2.write(regPg+'\n')
					#newUrl = getRedirectedLink(regPg)
					#if newUrl is not None:
					#	fout2.write(newUrl+'\n')
	fin.close()
	fout.close()
	fout2.close()
	#print "%s: %s %s \n" %(threadName, ipFile, time.ctime(time.time()))
	  
for fl in range(1, totFiles+1):
	name = 'Thread-'+str(fl*entries)
	fileName = 'split_file_'+str(fl*entries)+'.txt'
	print 'Thread Name: '+name+' Input File Name: '+fileName
	#Create two threads as follows
	try:
		thread.start_new_thread( process_urls, (name, fileName, ) )
		#thread.start_new_thread( print_time, ("Thread-2", 4, ) )
	except:
		print "Error: unable to start thread"

print '************************************'
print 'Uniting all the split files into one'
filenames = glob2.glob('*out.txt')  # list of all .txt files in the directory

with open('activeDomains.txt', 'w') as f:
    for file in filenames:
        with open(file) as infile:
            f.write(infile.read()+'\n')
print '************************************'
print 'DONE !!'
while 1:	
	pass
