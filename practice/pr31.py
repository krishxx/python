# -*- coding: utf-8 -*-
"""
Created on Sun May 27 07:11:47 2018

@author: Srikrishna.Sadula
"""

def printValue(s1,s2):
	len1 = len(s1)
	len2 = len(s2)
	if len1>len2:
		print (s1)
	elif len2>len1:
		print (s2)
	else:
		print (s1)
		print (s2)
		
#s1 = input()
#s2 = input()
s1 = "hy\b"
s2 = "secad\b"

print(s2, s1, end='')
#print(s1)
#printValue(s1,s2)