'''
128. Write a program to Print Table of a Given Number
'''
num=int(input("enter number for which table to be printed: "))

for i in range(0,21):
	print("%d * %d = %d "% (num,i,num*i))