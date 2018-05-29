# -*- coding: utf-8 -*-
"""
Created on Tue May 29 06:07:25 2018

@author: Srikrishna.Sadula
"""

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input())
print (fact(x))