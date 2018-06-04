# -*- coding: utf-8 -*-
"""
Created on Wed May 23 07:01:09 2018

@author: Srikrishna.Sadula
"""

class Parent(object):
    def implicit(self):
        print ("PARENT implicit()")
        return "parent implicit"
class Child(Parent):
    pass

dad = Parent()
son = Child()


print("calling parent object: ", dad.implicit())
print("calling child object: ", son.implicit())