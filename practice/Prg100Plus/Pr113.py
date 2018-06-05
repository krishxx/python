'''
113. Write a program to Count the Number of Digits in a Number
'''
num=int(input("enter a number: "))
count=0
while num!=0:
	count=count+1
	num = int(num/10)
print(count)	
	