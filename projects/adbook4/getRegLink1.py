#!/usr/bin/python
import re
import sys
import validators
import urllib2
#import scrapy
import httplib
import time
from time import gmtime, strftime
import thread
from itertools import izip_longest
import glob, os
import glob2
import urllib
import requests
from bs4 import BeautifulSoup
import time

def process_iframe(url):
	print url
'''
	driver = webdriver.Firefox()
	driver.implicitly_wait(10)
	driver.get(url)
	try:
		time.sleep(4)
		iframe = driver.find_elements_by_tag_name('iframe[id=icims_formFrame]')[0]
		driver.switch_to_default_content()

		driver.switch_to_frame(iframe)
		driver.find_elements_by_tag_name('iframe')[0]

		output = driver.page_source
		print output		
	finally:
		driver.quit()
'''
def process_url(url, fileOutHandle, fileOutHandle2):
	filterFlag = 0
	regToks = ['register', 'registration', 'Register', 'Registration', 'Portal_Registration', 'Register Now', 'sign up', 'Sign up', 'signup', 'Signup', 'SIGN UP', 'Sign Up', 'Join', 'join', 'Join me', 'Join Me', 'Join Us', 'Join us', 'membership', 'registrierung', 'registrazione', 'subscription', 'subscribe', 'registro', 'Create', 'Create User', 'Create Account', 'create account', 'Create account', 'open account', 'Open Account', 'Open account'] #'contact', 'Contact', 'mail', 'webmail', 'login', 'Login', 'sign']#'twitter', 'facebook', account
	if 'http' not in url:
		url = 'https://'+url
		#print url
        if (('.edu' in url) or ('.gov' in url) or ('.ac.' in url) or ('career' in url)):
                return;
	try:
		url = url.rstrip()
		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')
		for a in soup.find_all('a', href=True):
			for tok in regToks:
				if (tok in a['href']) and (('http' in a['href']) or ('www.' in a['href'])):
                                        if (('mailto:' not in a['href']) and ('design' not in a['href']) and ('campus' not in a['href']) and ('gov' not in a['href']) and ('support' not in a['href']) and ('edu' not in a['href']) and ('career' not in a['href']) and ('linkedin' not in a['href']) and ('facebook' not in a['href'])):
						print "Found the URL: ", a['href']
						fileOutHandle.write(a['href']+'\n')
						#print "associated token :", tok 
						filterFlag = 1
						break;
			if(filterFlag == 1):
				break;
		if(filterFlag == 0):
                        for tok2 in regToks:
				tags = soup.body.find_all(string=re.compile('.*{0}.*'.format(tok2)), recursive=True)
				#print 'tags:tok2', tags, tok2
                                if (len(tags) > 0):
                                        fileOutHandle2.write(url+'\n')
                                        #print "associated tags:", tags
                                        break;
		soup.close()		
		page.close()
	except:
		print '.'

def process_file(ipfile, opfile, opfile2):
	fin = open(ipfile, "r")
	fout = open(opfile, "w")
	fout2 = open(opfile2, "w")
	for line in fin:
		#print line;
		url = line.split()
		process_url(url[0], fout, fout2);
	fin.close()
	fout.close()


process_file('sample.txt', 'sampleOut.txt', 'probableSampleOut.txt')
	
