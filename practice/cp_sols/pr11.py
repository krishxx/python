# -*- coding: utf-8 -*-
"""
Created on Wed May 30 06:11:19 2018

@author: Srikrishna.Sadula
"""

value = []
items=[x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print (','.join(value))
