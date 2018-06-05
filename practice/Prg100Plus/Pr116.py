'''
116. Write a program to Read a Number n And Print the Series "1+2+…..+n= "
'''
num=int(input("enter number"))
print(num*(num+1)/2)
tot=1
print(1,end='')
for i in range(2,num+1):
	print("+%d" % i,end='')
	tot=tot+i
print("=%d" % tot)