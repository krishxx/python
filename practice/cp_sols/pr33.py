# -*- coding: utf-8 -*-
"""
Created on Mon May 28 06:23:53 2018

@author: Srikrishna.Sadula
"""

def printDict():
    d=dict()
    d[1]=1
    d[2]=2**2
    d[3]=3**2
    d[4]=4**2
    print (d)


#pr34
def printDict2():
    d = dict()
    for i in range(1, 21):
        d[i] = i**2
    print(d)
    
    		
printDict()
printDict2()