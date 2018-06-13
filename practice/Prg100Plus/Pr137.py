'''
137. Write a program to Find the LCM of Two Numbers
'''

def gcd (num1,num2):
	if num1%num2==0:
		return num2
	else:
		return gcd(num2,num1%num2)

num1=int(input("enter num1: "))
num2=int(input("enter num2: "))

print("LCM(%d , %d)=%d"%(num1,num2,num1*num2/gcd(num1,num2)))