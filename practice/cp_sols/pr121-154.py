# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 14:41:20 2018

@author: srikrishna.sadula
"""
'''
-----------------Examples on Mathematical Functions-------------------
'''

'''
121. Write a program to Check if a Date is Valid and Print the Incremented Date if it is
'''
import re
def date_validation(datestr):
    items = re.findall(r'\d+', datestr)
    day = int(items[0])
    month = int(items[1])
    year = int(items[2])
    if((day>0 and day<32) and (month>0 and month<13) and (year>1 and year<3000)):
        day=day+1
        print(str(day)+':'+str(month)+':'+str(year))
    else:
        print ('Invalid date')

print ("print date in format dd:mm:yyyy or dd-mm-yyyy")
datestr = input()
date_validation(datestr)

'''
122. Write a program to Compute Simple Interest Given all the Required Values
'''
def si(p, n, r):
    return (p*n*r)/100

print ("Enter principal Amt")
principalamt = int(input())
print ("Enter no.ofyears") 
noofyears = int(input())
print ("Enter rate of interest")
rateofinterest = int(input())
print ("simple interest calculated =", si(principalamt, noofyears, rateofinterest))
'''
123. Write a program to Check Whether a Given Year is a Leap Year
'''

def check_leap_year(year):
    if((year%4==0) or ((year%100==0) and (year%400==0))):
        print ("Its Leap year")
    else:
        print ("Its not leap year")

check_leap_year(1996)
        
'''
124. Write a program to Read Height in Centimeters and then Convert the Height to Feet and Inches
'''

'''
125. Write a program to Take the Temperature in Celcius and Covert it to Farenheit
126. Write a program to Compute Prime Factors of an Integer
127. Write a program to Generate all the Divisors of an Integer
128. Write a program to Print Table of a Given Number
129. Write a program to Print Sum of Negative Numbers, Positive Even Numbers and Positive Odd numbers in a List
130. Write a program to Print Largest Even and Largest Odd Number in a List
131. Write a program to Form an Integer that has the Number of Digits at Ten's Place and the Least Significant Digit of the Entered Integer at One's Place
132. Write a program to Find Those Numbers which are Divisible by 7 and Multiple of 5 in a Given Range of Numbers
134. Write a program to Check if a Number is an Armstrong Number
135. Write a program to Print the Pascal's triangle for n number of rows given by the user
136. Write a program to Check if a Number is a Perfect Number
137. Write a program to Check if a Number is a Strong Number
138. Write a program to Find the LCM of Two Numbers
139. Write a program to Find the GCD of Two Numbers
140. Write a program to Compute a Polynomial Equation given that the Coefficients of the Polynomial are stored in a List
141. Write a program to Check If Two Numbers are Amicable Numbers
142. Write a program to Find the Area of a Triangle Given All Three Sides
143. Write a program to Find the Gravitational Force Acting Between Two Objects
144. Write a program to Check if a Number is a Prime Number
145. Write a program to Print all the Prime Numbers within a Given Range
146. Write a program to Print Numbers in a Range (1,upper) Without Using any Loops
147. Write a program to Find the Sum of Sine Series
148. Write a program to Find the Sum of Cosine Series
149. Write a program to Find the Sum of First N Natural Numbers
150. Write a program to Find the Sum of the Series: 1 + 1/2 + 1/3 + ….. + 1/N
151. Write a program to Find the Sum of the Series: 1 + x^2/2 + x^3/3 + … x^n/n
152. Write a program to Compute the Value of Euler's Number e. Use the Formula: e = 1 + 1/1! + 1/2! + …… 1/n!
153. Write a program to Determine all Pythagorean Triplets in the Range
154. Write a program to Search the Number of Times a Particular Number Occurs in a List
'''