# -*- coding: utf-8 -*-
"""
Created on Mon May 28 06:35:00 2018

@author: Srikrishna.Sadula
"""
d = dict()

def makeDict():
    for i in range(1, 21):
        d[i] = i**2
        print (d[i], end=',')
    print('\n')

def printDictVals():
    for (k,v) in d.items():
        print (v, end=',')
  		
makeDict()
printDictVals()