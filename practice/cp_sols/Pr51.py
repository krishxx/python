'''
Question: 51)

Define a class named American and its subclass NewYorker. 

Hints:

Use class Subclass(ParentClass) to define a subclass.

Solution:'''

class American(object):
    pass

class NewYorker(American):
    pass

anAmerican = American()
aNewYorker = NewYorker()
print(type(anAmerican))
print (anAmerican)
print (aNewYorker)
print ("abcdef123")