'''
119. Write a program to Print an Inverted Star Pattern
'''
num=int (input("enter number: "))

for i in range(0,num):
	for j in range(0,num-i):
		print("*",end=' ')
	print("\n")