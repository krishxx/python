# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 10:29:14 2018

@author: Srikrishna.Sadula
"""

'''
Question:
101. Write a program to Calculate the Average of Numbers in a Given List

Solution:
'''
li = [1,2,3,4]
s = 0
for i in li:
    s = s + i
avg = s/li.__len__()

print ("average of given list :", avg)

'''
102. Write a program to Exchange the Values of Two Numbers Without Using a Temporary Variable
'''
a = int(input())
b = int(input())

a = a+b
b = a-b
a = a-b
print (a, b)

'''
103. Write a program to Read a Mumber n and Compute n+nn+nnn
'''
n = int(input())
res = n + n*n + n*n*n
print (res)
'''
104. Write a program to Reverse a Given Number
'''
n = int(input())
print ("Given no. is :", n)
n1 = 0
while (n>0):
    n1 = n1*10 + int(n%10);
    #print (n1)
    n = int(n/10)
    #print (n)
print ("reversed no is", n1)
'''
105. Write a program to Check Whether a Number is Positive or Negative
'''
def checkPosNeg(a):
    if(a>0):
        print (a, "is positive")
    else:
        print (a, "is negative")
        
checkPosNeg(20)
checkPosNeg(-20)
checkPosNeg(int(input()))
'''
106. Write a program to Take in the Marks of 5 Subjects and Display the Grade
'''
def display_grade():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    s = (a+b+c+d+e)/5
    if(s>=60):
        print("I Grade")
    elif(s>=50):
        print("II Grade")
    elif(s>=35):
        print("III Grade")
    else:
        print("Fail")
display_grade()
    
'''
107. Write a program to Print all Numbers in a Range Divisible by a Given Number
'''

'''
108. Write a program to Read Two Numbers and Print Their Quotient and Remainder
109. Write a program to Accept Three Digits and Print all Possible Combinations from the Digits
110. Write a program to Print Odd Numbers Within a Given Range
111. Write a program to Find the Sum of Digits in a Number
112. Write a program to Find the Smallest Divisor of an Integer
113. Write a program to Count the Number of Digits in a Number
114. Write a program to Check if a Number is a Palindrome
115. Write a program to Print all Integers that Aren't Divisible by Either 2 or 3 and Lie between 1 and 50.
116. Write a program to Read a Number n And Print the Series "1+2+…..+n= "
117. Write a program to Read a Number n and Print the Natural Numbers Summation Pattern
118. Write a program to Print an Identity Matrix
119. Write a program to Print an Inverted Star Pattern
120. Write a program to Read Print Prime Numbers in a Range using Sieve of Eratosthenes
'''