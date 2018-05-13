# -*- coding: utf-8 -*-
"""
Created on Sun May 13 07:41:21 2018

@author: Srikrishna.Sadula
"""

from sys import argv
script, filename = argv
txt = open(filename)
print ("Here's your file %r:" % filename)
print (txt.read())
print ("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)
print (txt_again.read())