'''
134. Write a program to Print the Pascal's triangle for n number of rows given by the user
'''
row=int(input("enter no of rows: "))

def fact(i):
	retv=1
	for i in range(2,i+1):
		retv=retv*i
	return retv
	
for i in range(0,row):
	for j in range(0,i+1):
		print(int(fact(i)/(fact(j)*fact(i-j))), end=" ")
	print("\n")
	