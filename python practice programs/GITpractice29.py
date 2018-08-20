# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 14:00:33 2018

@author: Harsh
"""

'''
Define a function which can print a dictionary where the keys are numbers between 1 and 20 
(both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
'''
def dictionary():
    d = dict()
    for i in range(1,21):
        d[i] = i**2
    print(d,"\n\t")