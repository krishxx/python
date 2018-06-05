'''
115. Write a program to Print all Integers that Aren't Divisible by Either 2 or 3 and Lie between 1 and 50.
'''
for i in range(1,51):
	if i%2!=0 or i%3!=0:
		print(i)
		
	