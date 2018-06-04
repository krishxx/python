'''
110. Write a program to Print Odd Numbers Within a Given Range
'''
print("enter the range of number")
lft= int(input("leftinclusive: "))
rgt=int(input("leftinclusive: "))
for i in range(lft,rgt+1):
	if i%2==1:
		print(i,end=' ')
		