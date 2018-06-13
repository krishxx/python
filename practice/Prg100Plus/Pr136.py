'''
136. Write a program to Check if a Number is a Strong Number
'''
def fact(i):
	retv=1
	for i in range(2,i+1):
		retv=retv*i
	return retv

num=int(input("enter num: "))
num1=num
sm=0
while num1!=0:
	ld=int(num1%10)
	sm=sm+fact(ld)
	num1=int(num1/10)
if sm==num:
	print("number %d is Strong number" %num)
else:
	print("number %d is NOT Strong number" %num)