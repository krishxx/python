# -*- coding: utf-8 -*-
"""
Created on Fri May 18 07:26:12 2018

@author: Srikrishna.Sadula
"""

i = 0
numbers = []
while i < 6:
    print ("At the top i is %d" % i)
    numbers.append(i)
    i = i + 1
    print ("Numbers now: ", numbers)
    print ("At the bottom i is %d" % i)

print ("The numbers: ")
for num in numbers:    
    print (num)
    
var = 22
for i in var:
    print (i)