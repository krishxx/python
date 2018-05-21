# -*- coding: utf-8 -*-
"""
Created on Sun May 20 06:18:13 2018

@author: Srikrishna.Sadula
"""

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print ("Wait there's not 10 things in that list, let's fix that.")
stuff = ten_things.split(' ')
print (stuff)
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print ("Adding: ", next_one)
    stuff.append(next_one)
    print ("There's %d items now." % len(stuff))
    
print ("There we go: ", stuff)
print ("Let's do some things with stuff.")
print (stuff[1])
print (stuff[- 1]) # whoa! fancy
print (stuff.pop())
print (' '.join(stuff)) # what? cool!
things = ' '.join(stuff)
print (things)
print ('#'.join(stuff[0:3])) # super stellar!
print(''.join(stuff[0:-2]))