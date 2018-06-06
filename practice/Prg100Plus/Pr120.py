'''
120. Write a program to Read Print Prime Numbers in a Range using Sieve of Eratosthenes
'''
num=int(input("enter num"))
rlist=list()
plist=list()
for i in range(2,num+1):
	rlist.append(i)
for i in rlist:
	#plist.append(i)
	print (i)
	rlist = [x for x in rlist if x%i!=0 or x==i]
#print(plist)
print(rlist)