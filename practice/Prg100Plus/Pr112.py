'''
112. Write a program to Find the Smallest Divisor of an Integer
'''

num=int(input("enter a number for which smallest divisor is to be found: "))
i=5
if num%2==0:
	print(2)
elif num%3==0:
	print(3)
else:	
	while i < int(num/5):
		if(num%i==0):
			print (i)
			break
		else:
			i=i+1
	print("Prime number")