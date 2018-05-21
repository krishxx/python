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
class Calculator(object):
    def __init__(self, item1, item2, operation):
        self.item1=item1
        self.item2=item2
        self.operation=operation
    def calculate_operation(self):
        if self.operation == '+':
            print (self.item1+self.item2)
        if self.operation == '-':
            print (self.item1-self.item2)
        if self.operation == '/':
            print (self.item1/self.item2)
        if self.operation == '*':
            print (self.item1*self.item2)
            
cal_addition = Calculator([1],[2],['+'])
cal_subtraction = Calculator()
cal_addition.calculate_operation()