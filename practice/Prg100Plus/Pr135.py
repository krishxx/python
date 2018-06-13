'''
135. Write a program to Check if a Number is a Perfect Number
'''
num=int(input("enter num: "))
sum=1
for i in range(2,num):
	if num%i==0:
		sum=sum+i
if sum==num:
	print("num :%d is Perfect number" %num)
else:
	print("num :%d is NOT Perfect number" %num)

