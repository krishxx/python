'''
126. Write a program to Compute Prime Factors of an Integer
'''
num=int(input("enter num to compute its prime factors: "))

rlist=list()
plist=list()
for i in range(2,num+1):
	rlist.append(i)
for i in rlist:
	rlist = [x for x in rlist if x%i!=0 or x==i]

for i in rlist:
	if num%i==0:
		plist.append(i)

print("prime facctors are: ",plist)