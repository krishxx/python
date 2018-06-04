'''
Question: 83

Please write a program to print the running time of execution of "1+1" for 100 times.



Hints:
Use timeit() function to measure the running time.

Solution:
'''
from timeit import Timer
j=0
t = Timer("for i in range(0,10): 1+1")
print (t.timeit())

