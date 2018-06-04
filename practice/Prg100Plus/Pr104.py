'''
104. Write a program to Reverse a Given Number
'''
num=int(input())
revnum=0
while num!=0:
	revnum=revnum*10+num%10
	num=(int)(num/10)
	#print(revnum,num)
print(revnum)
