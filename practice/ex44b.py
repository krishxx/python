# -*- coding: utf-8 -*-
"""
Created on Fri May 25 17:33:21 2018

@author: Srikrishna.Sadula
"""

class Parent(object):
    def override(self):
        print ("PARENT override()")
class Child(Parent):
    def override(self):
        print ("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()