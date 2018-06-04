'''
106. Write a program to Take in the Marks of 5 Subjects and Display the Grade
'''
print("enter  marks")
a=int(input("Mathematics: "))
b=int(input("English: "))
c=int(input("Science: "))
d=int(input("Social: "))
e=int(input("Hindi: "))
avg=(a+b+c+d+e)/5
if(a>39 and b>39 and c>39 and d>39 and e>39):
	if avg>=80:
		print("Distinction")
	elif avg>=60:
		print("First class")
	elif avg>=50:
		print("Second Class")
	else:
		print("Third Class")
else:
	print("Failed")
	


