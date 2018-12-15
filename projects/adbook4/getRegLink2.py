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
def check_content(url, word):
        page = requests.get(url)
        visibleText = re.sub("(\<.*?\>)", "",page.content)
        if word in visibleText:
                return True
	else:
		return False

def process_url(url, fileOutHandle, fileOutHandle2):
	filterFlag = 0
	counter1 = 1
	counter2 = 1
	regToks = ['register', 'registration', 'Register', 'Registration', 'Portal_Registration', 'Register Now', 'sign up', 'Sign up', 'signup', 'Signup', 'SIGN UP', 'Sign Up', 'Join', 'join', 'Join me', 'Join Me', 'Join Us', 'Join us', 'registrierung', 'registrazione', 'registro', 'Create', 'Create User', 'Create Account', 'create account', 'Create account', 'open account', 'Open Account', 'Open account'] #'contact', 'Contact', 'mail', 'webmail', 'login', 'Login', 'sign']#'twitter', 'facebook', 'account', 'subscribe', 'subscription', 'membership'

	regToks2 = ['mail', 'Confirm Email', 'confirm email', 'University', 'university','college', 'College', 'School', 'school', 'Bank','bank', 'career', 'mail *','Email', 'E-Mail', 'E-mail*','email_validation','Student', 'student', 'Conference', 'conferenc', 'Publications', 'publication','Journal', 'journal', 'Event', 'event', 'Event Registration', 'event registration', 'Vodafone', 'vodafone', 'Airtel', 'airtel', 'AnnualPrice', 'Annual Price', 'Price', 'price', 'business', 'Subscribe', 'subscribe', 'email', 'classes', 'health', 'invest', 'loan', 'team', 'partnership', 'fashion', 'Fashion', 'Foot', 'foot', 'Insurance', 'insurance', 'finance', 'Finance', 'Ministry', 'Suppliers', 'suppliers', 'Admission', 'admission', 'studies', 'research', 'Research', 'oil', 'environment', 'Landlords', 'landlords', 'surgery', 'Surgery', 'patients', 'Patients']
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
				counter1 = counter1 + 1
				if (tok in a['href']) and (('http' in a['href']) or ('www.' in a['href'])):
					if (('mailto:' not in a['href']) and ('design' not in a['href']) and ('campus' not in a['href']) and ('gov' not in a['href']) and ('support' not in a['href']) and ('edu' not in a['href']) and ('career' not in a['href']) and ('Career' not in a['href']) and ('linkedin' not in a['href']) and ('facebook' not in a['href']) and ('bank' not in a['href']) and ('careers' not in a['href']) and ('event' not in a['href']) and ('school' not in a['href']) and ('student' not in a['href']) and ('university' not in a['href']) and ('college' not in a['href']) and ('bank' not in a['href']) and ('health' not in a['href']) and ('business' not in a['href']) and ('shop' not in a['href']) and ('store' not in a['href']) and ('market' not in a['href']) and ('venture' not in a['href']) and ('structure' not in a['href']) and ('agents' not in a['href']) and ('Agents' not in a['href']) and ('partnership' not in a['href']) and ('product' not in a['href']) and ('training' not in a['href']) and ('campaign' not in a['href']) and ('SHOP' not in a['href']) and ('investor' not in a['href']) and ('joint' not in a['href']) and ('Joint' not in a['href']) and ('classes' not in a['href']) and ('invest' not in a['href']) and ('vodafone' not in a['href']) and ('airtel' not in a['href']) and ('loans' not in a['href']) and ('Bank' not in a['href'])):
						page2 = requests.get(a['href'])
						visibleText = re.sub("(\<.*?\>)", "",page2.content)	
						for tok2 in regToks2:
							if(tok2 not in visibleText):
								counter2 = counter2 + 1
							else:
								filterFlag = 2
								counter2 = 0
								break;
						page2.close()
			if(filterFlag == 2):
				break;
			elif(counter2 >= len(regToks2)):
				print "Found the URL: ", a['href']
				fileOutHandle.write(a['href']+'\n')
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
		#url = line.split()
		process_url(line, fout, fout2);
	fin.close()
	fout.close()


process_file('latest_Out.txt', 'latest_Out2.txt', 'probable_latest_Out.txt')
