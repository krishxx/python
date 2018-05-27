# -*- coding: utf-8 -*-
"""
Created on Sun May 27 07:25:48 2018

@author: Srikrishna.Sadula
"""

def checkValue(n):
    if n%2 == 0:
        print ("It is an even number")
        val = 1
    else:
        print ("It is an odd number")
        val = 0
    
    return val


#checkValue(7)
if(checkValue(8) == 1):
    print ("even number")