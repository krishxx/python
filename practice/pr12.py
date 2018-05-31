# -*- coding: utf-8 -*-
"""
Created on Wed May 30 06:33:16 2018

@author: Srikrishna.Sadula
"""

values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print (",".join(values))