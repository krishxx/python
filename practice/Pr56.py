'''Question: 56

Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints:

Use try/except to catch exceptions.

Solution:
'''
def throws():
	5/0
	#err
	print("tintintitin")
	return

try:
    throws()
except ZeroDivisionError:
    print ("division by zero!")
except Exception:
    print ('Caught an exception')
finally:
    print ('In finally block for cleanup')