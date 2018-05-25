# -*- coding: utf-8 -*-
"""
Created on Fri May 25 06:14:43 2018

@author: Srikrishna.Sadula
"""
l = []
for i in range(2000, 3000):
    if (i%7==0) and (i%5 != 0):
        print (i, end=',')
        l.append(i)
        
print (l)