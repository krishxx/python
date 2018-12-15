#!bin/python
import os
import time
from time import gmtime, strftime

print "\n*****HELLO ADDRESSBOOK*********"
print "***TIME: "+strftime("%Y-%m-%d %H:%M:%S***", gmtime())
print "*******************************"

def test():
	fp=open("testlog.txt","w")
	for i in range(100000):
		time.sleep(60)
		print i
		print ">>TIME:"+strftime("%Y-%m-%d %H:%M:%S***", gmtime())
		fp.write('instance :'+str(i))
		fp.write('TIME:'+strftime('%Y-%m-%d %H:%M:%S***', gmtime()))
	fp.close()
	return
test()
