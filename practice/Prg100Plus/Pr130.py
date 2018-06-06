'''
130. Write a program to Print Largest Even and Largest Odd Number in a List
'''
li=list()
print("enter numbers in to the list")
num=input()
while num!='':
	li.append(int(num))
	num=input()
sz=len(li)
i=0
lo=-1
le=-1
while i<sz:
	if li[i]%2==0 and li[i]>le:
		le=li[i]
		i=i+1
	elif li[i]%2!=0 and li[i]>lo:
		lo=li[i]
		i=i+1
		
print("Largest even: %d and Largest Odd: %d in the list" %(le,lo))
		