'''
Question: 85

Please write a program to shuffle and print the list [3,6,7,8].



Hints:
Use shuffle() function to shuffle a list.

Solution:
'''
from random import shuffle
li = [3,6,7,8]
a=li[0]
shuffle(li)
b=li[0]
print (a,b)
print(li)
