# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 15:08:43 2018

@author: Harsh
"""

'''
Define a function which can print a dictionary 
where the keys are numbers between 1 and 3 (both included)
and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
'''
def dictionary():
    d = dict()
    d[1] = 1
    for i in range(1,3):
        d[i] = i**i
    print(dictionary())    