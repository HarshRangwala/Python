# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 16:45:40 2018

@author: Harsh
"""

'''
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
'''
def num(n):
    i=0
    while i<n:
        j=i
        i=i+1
        if i % 7 ==0:
            yield j
for i in reverse(100):
    print (i)