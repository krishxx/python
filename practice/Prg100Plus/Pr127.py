'''
127. Write a program to Generate all the Divisors of an Integer
'''
num=int(input("enter num to compute its all divisors: "))
dlist=list()
'''
if num%2==0:
	dlist.append(2)
	dlist.append(int(num/2))
if num%3==0:
	dlist.append(3)
	dlist.append(int(num/3))
'''	
big=num
for i in range(1,num+1):
	if i>=big:
		break
	if num%i==0:
		dlist.append(i)
		big=int(num/i)
		dlist.append(big)
			
print (dlist)