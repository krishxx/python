# -*- coding: utf-8 -*-
"""
Created on Sun May 20 07:33:16 2018

@author: Srikrishna.Sadula
"""

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print (line)
            
happy_bday = Song(["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"])
bulls_on_parade = Song(["They rally around the family",
"With pockets full of shells"])
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()


#Write a program to implement calculator using class
'''
class Calculator(object):
    def __init__(self, items, operation):
        self.items = items        
        self.operation=operation
    def calculate_operation(self):
        if self.operation == '+':
            print(self.itmes)
            print (self.items[0]+self.items[1])
        if self.operation == '-':
            print (self.items[0]-self.items[1])
        if self.operation == '/':
            print (self.items[0]/self.items[1])
        if self.operation == '*':
            print (self.items[0]*self.items[1])
            
cal_addition = Calculator([1,2],['+'])
cal_addition.calculate_operation()
'''
    
class Calculator(object):
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
    def add(self):
        return sum(self.val1, self.val2)

c1 = Calculator(2,3)
print (c1.add())