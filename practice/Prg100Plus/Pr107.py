'''107. Write a program to Print all Numbers in a Range Divisible by a Given Number
'''
print("enter the number")
num=int(input())
print("enter range")
lft=int(input("left inclusive: "))
rgt=int(input("right inclisive: "))
li=list()
for i in range(lft,rgt+1):
	if(i%num==0):
		li.append(i)
		print(i ,end=' ')
print("\r\n",li)