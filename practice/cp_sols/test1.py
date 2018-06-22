# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:20:23 2018

@author: Srikrishna.Sadula
"""

a=[]
even = []
odd = []
n=int(input("enter number of elements:"))
for i in range(1,n+1):
    b=int(input("enter element:"))
    a.append(b)
    if (b%2 == 0):
        even.append(b)
    else:
        odd.append(b)

print("all numbers:", a)
print("even numbers:",even)
print("odd numbers:",odd)