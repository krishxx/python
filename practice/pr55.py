# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 07:16:49 2018

@author: Srikrishna.Sadula
"""

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(type(map(lambda x: x**2, items)))

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
print(type(filter(lambda x: x < 0, number_list)))