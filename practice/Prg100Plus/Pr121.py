'''
121. Write a program to Check if a Date is Valid and Print the Incremented Date if it is
'''
date=int(input("enter date in DDMMYYYY: "))
year=date%10000
mon=(int(date/10000))%100
day=int(date/1000000)
valid=1
if mon>12 or mon<1:
	valid=0
	print(" invalid month")
elif mon in [1,3,5,7,8,10,12]:
	if day>31 or day<1:
		valid=0
		print("invalid day")
elif mon in [4,6,9,11]:
	if day>30 or day<1:
		valid=0
		print("invalid day")
else:
	if (year%4==0 and year%100!=0) or year%400==0:
		if day>29 or day<1:
			valid=0
			print("invalid day")
	else:
		if day>28 or day<1:
			valid=0
			print("invalid day")
if valid==1:
	print("valid")
	incdays=int(input("enter no of days to increment: "))
	
			