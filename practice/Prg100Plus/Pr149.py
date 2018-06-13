'''
150. Write a program to Find the Sum of the Series: 1 + 1/2 + 1/3 + ….. + 1/N
'''

num=int(input("enter N: "))
sum=0
for i in range(1, num+1):
	sum=sum+1/i
	
print("sum of series 1 + 1/2 + ….. + 1/%d is : %f" %(num,sum))	