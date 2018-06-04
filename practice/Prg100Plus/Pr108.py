'''
108. Write a program to Read Two Numbers and Print Their Quotient and Remainder
'''

num1=int(input("enter Dividend: "))
num2=int(input("enter Divisor: "))
try:
	print("Quiotient: %d Reminder: %d" % (int(num1/num2) , num1%num2)) 
except ZeroDivisionError:
    print ("Exception: division by zero!")
finally:
	print ("bye bye")