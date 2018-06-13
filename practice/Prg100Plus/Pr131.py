'''
131. Write a program to Form an Integer that has the Number of Digits at Ten's Place and the Least Significant Digit of the Entered Integer at One's Place
'''
num=int(input("enter number"))
formednum=num%10
count=0
while num:
	count=count+1
	num=int(num/10)
formednum+=count*10	
print("formed num is: %d " %formednum)
