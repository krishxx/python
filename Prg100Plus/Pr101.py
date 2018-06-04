'''
101. Write a program to Calculate the Average of Numbers in a Given List
'''

li=[1,2,13,4,5]
cnt=len(li)
su=0;
try:
	for i in li:
		su=su+i
	print(su,cnt)	
	avg=float(su)/cnt
	print(avg)
except ZeroDivisionError:
    print ("division by zero!")
except Exception:
    print ('Caught an exception')
finally:
    print ('In finally block for cleanup')
