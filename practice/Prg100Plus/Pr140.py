'''
140. Write a program to Check If Two Numbers are Amicable Numbers
'''
num1=int(input("enter num1"))
num2=int(input("enter num2"))
#dlis1=list()
#dlis2=list()

sum1=1
sum2=1
for i in range (2,int(num1/2)+2):
	if num1%i==0:
		sum1=sum1+i
		#dlis1.append(i)
for i in range (2,int(num2/2)+2):
	if num2%i==0:
		sum2=sum2+i
		#dlis2.append(i)
if sum1==num2 and sum2==num1:
	print("Amicable")
else:
	print("Not Amicable")