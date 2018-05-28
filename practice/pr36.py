# -*- coding: utf-8 -*-
"""
Created on Mon May 28 06:44:43 2018

@author: Srikrishna.Sadula
"""

def printDict():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    for k in d.keys():	
        print (k, end=',')
    print(" ")
    for v in d.values():	
        print (v, end=',')		

printDict()