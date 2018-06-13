'''
151. Write a program to Find the Sum of the Series: 1 + x^2/2 + x^3/3 + … x^n/n
'''
x=int(input("enter x: "))
num=int(input("enter N: "))
sum=1
for i in range(2, num+1):
	sum=sum+(x**i/i)
	
print("sum of series 1 + x^2/2 + x^3/3 + … x^%d/%d is : %f" %(num,num,sum))	