'''
120. Write a program to Read Print Prime Numbers in a Range using Sieve of Eratosthenes
'''

num=int(input("enter num"))
rlist=list()
plist=list()
for i in range(2,num+1):
	rlist.append(i)
plist.append(2)
for i in plist:
	plist.append(i)
	k=i+i
	if k in rlist:
		rlist.remove(k)
		k=k+i	
print(plist)