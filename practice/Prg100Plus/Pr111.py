'''
111. Write a program to Find the Sum of Digits in a Number
'''
num=int(input("enter number: "))
sm=0
while num:
	sm=sm+num%10
	num=int(num/10)
print(sm)
