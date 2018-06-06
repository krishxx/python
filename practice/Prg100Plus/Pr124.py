'''
124. Write a program to Read Height in Centimeters and then Convert the Height to Feet and Inches
'''
cms=float(input("enter centimeters: "))
inc=cms/2.54
fee=int(inc/12)
rei=inc%12
print("%f cms = %d feet and %f inches" % (cms,fee,rei))
