# -*- coding: utf-8 -*-
"""
Created on Tue May 29 11:09:56 2018

@author: Srikrishna.Sadula
"""

input_str = input()
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col

print (multilist)