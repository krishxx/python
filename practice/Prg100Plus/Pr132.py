'''
132. Write a program to Find Those Numbers which are Divisible by 7 and Multiple of 5 in a Given Range of Numbers
'''

nulf=int(input("enter num left range"))
nurt=int(input("enter num right range"))
li7a5=list()
li7o5=list()
for i in range(nulf,nurt+1):
	if i%35==0:
		li7a5.append(i)
	if i%7==0 or i%5==0:
		li7o5.append(i)
		
print(li7a5)
print(li7o5)
		
