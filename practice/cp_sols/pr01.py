# -*- coding: utf-8 -*-
"""
Created on Sun May 27 06:21:09 2018

@author: Srikrishna.Sadula
"""

def fact(var):
    fact_val = 1
    for i in range (1, var):
        fact_val = i * fact_val
    print ("factorial of ", var, "is", fact_val)
    return fact_val

def some_prog(var):
    a = fact(2) * fact(var)
    print ("sum_prog:", a)
    
some_prog(4)

numbers = [2.5, 3, 4, -5]

# start parameter is not provided
numbersSum = sum(numbers)
print(numbersSum)

# start = 10
numbersSum = sum(numbers, 10)
print(numbersSum)

