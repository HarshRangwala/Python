# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 02:25:32 2020

@author: Anuj
"""


#s = "MHM's outcome cased education"
s = "try and work on pythonista"
def even_length_word(s):
    string = []
    count = 0
    for i in s.split():
        #print(len(i))
        if len(i)%2 == 0:
            string.append(i)
            count+=0
    return tuple(string)
print(even_length_word(s)) 
    