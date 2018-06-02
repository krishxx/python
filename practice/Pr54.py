'''Question: 54

Define a class named Shape and its subclass Square. The Square class has an 
init function which takes a length as argument. Both classes have a area 
function which can print the area of the shape where Shape's area is 0 by default.

Hints:

To override a method in super class, we can define a method with the same name
 in the super class.

Solution:
'''
class Shape(object):
    def __init__(self):
        self.l = 10
        pass

    def area(self):        
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.l = 1

    def area(self):
        return self.l * self.l
        #return self.length*self.length
    
class Circle(Shape):
    def __init__(self, r):
        Shape.__init__(self)
        self.radius = r

    def area(self):
        return self.radius**2*3.14


aSquare= Square(3)
aCircle = Circle(2)
print (aSquare.area())
print (aCircle.area())