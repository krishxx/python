'''
129. Write a program to Print Sum of Negative Numbers, Positive Even Numbers and Positive Odd numbers in a List
'''
li=list()
print("enter numbers in to the list")
num=input()
while num!='':
	li.append(int(num))
	num=input()
ln=len(li)
sn=0
spe=0
spo=0
for i in range(0,ln):
	if li[i]<0:
		sn=sn+li[i]
	elif li[i]%2==0:
		spe=spe+li[i]
	else:
		spo=spo+li[i]
print("sum of negative nos: %d \nsum of positive even nos: %d \nsum of positive odd nos: %d " %(sn,spe,spo))	
	
	