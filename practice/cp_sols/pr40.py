# -*- coding: utf-8 -*-
"""
Created on Mon May 28 07:03:21 2018

@author: Srikrishna.Sadula
"""

def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print (li[5:])
		
printList()