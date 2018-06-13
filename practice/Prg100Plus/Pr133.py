'''
133. Write a program to Check if a Number is an Armstrong Number
'''

num=int(input("enter number"))
asv=0
num1=num
ld=list()
while num1!=0:
	ld.append(num1%10)
	num1=int(num1/10)

pw=len(ld)
for i in ld:
	asv=asv+i**pw
if asv==num:
	print("given number: %d is Armstrong number" % num)
else:
	print("given number: %d is NOT Armstrong number" % num)