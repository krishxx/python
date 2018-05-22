# -*- coding: utf-8 -*-
"""
Created on Mon May 21 06:46:56 2018

@author: Srikrishna.Sadula
"""

import random
#from urllib2 import urlopen
from urllib.request import urlopen
import sys
WORD_URL = ("http://learncodethehardway.org/words.txt")
WORDS = []
PHRASES = {
"class %%%(%%%):":"Make a class named %%% that is-a %%%.",
"class %%%(object):\n\tdef __init__(self, ***)" : "class %%% has-a __init__ that takes self and *** parameters.",
"class %%%(object):\n\tdef ***(self, @@@)": "class %%% has-a function named *** that takes self and @@@ parameters.",
"*** = %%%()": "Set *** to an instance of class %%%.",
"***.***(@@@)": "From *** get the *** function, and call it with parameters self, @@@.",
"***.*** = '***'":"From *** get the *** attribute and set it to '***'."
}
# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    print (sys.argv[1])
    PHRASE_FIRST = True
# load up the words from the website
'''
for word in urlopen(WORD_URL).readlines():
    #print ("Inside a loop")       
    print (str(word), end='')
    WORDS.append(str(word.strip()))
'''
WORDS = [ 'account', 'achiever', 'actor', 'addition', 'adjustment']

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))
    for sentence in snippet, phrase:
        result = sentence[:]
    # fake class names
    for word in class_names:
        result = str(result.replace("%%%", str(word), 1))
    # fake other names
    for word in other_names:
        result = result.replace("***", word, 1)
        # fake parameter lists
    for word in param_names:
        result = result.replace("@@@", word, 1)
        results.append(result)
    return results
# keep going until they hit CTRL- D
try:
    snippets = []
    while True:
        print (PHRASES.keys())
        snippets = list(PHRASES.keys())
        print ("printing snippets->")
        print (snippets)
        random.shuffle(snippets)        
        print ("printing after shuffle", snippets)
        for snippet in snippets:            
            phrase = PHRASES[snippet]
            print (snippet, ':', phrase)
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
            print (question)
            input("> ")
            print ("ANSWER: %s\n\n" % answer)
except EOFError:
    print ("\nBye")