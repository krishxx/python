# -*- coding: utf-8 -*-
"""
Created on Tue May 29 11:07:33 2018

@author: Srikrishna.Sadula
"""

class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print (self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()