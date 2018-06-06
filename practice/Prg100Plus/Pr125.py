'''
125. Write a program to Take the Temperature in Celcius and Covert it to Farenheit
'''
cel=float(input("enter temp in celcius: "))
far=cel*9/5+32
print("%f Celcius = %f Farenheit" %(cel,far))

far=float(input("enter temp in farenheit: "))
cel=(far-32)*5/9 
print("%f Farenheit = %f Celcius" %(far,cel))
