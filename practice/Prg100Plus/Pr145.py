'''
146. Write a program to Print Numbers in a Range (1,upper) Without Using any Loops
'''
def recprint(upper):
	if upper>1:
		recprint(upper-1)
		print(upper, end=" ") 
	else:
		print(upper, end=" ")
		return

upper=int(input("enter upper limit: "))

recprint(upper)