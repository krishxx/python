'''
123. Write a program to Check Whether a Given Year is a Leap Year
'''
year=int(input("enter the year: "))
if (year%4 == 0 and year%100!=0) or year%400==0:
	print("Leap Year")
else:
	print("Not a Leap Year")
	
