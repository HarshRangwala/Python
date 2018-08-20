# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 14:54:18 2018

@author: Harsh
"""

'''
Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 
'''
def tuples():
    t = list()
    for i in range(1,21):
        t.append(i**2)
    print(tuple(t))
'''
With a given tuple (1,2,3,4,5,6,7,8,9,10), 
write a program to print the first half values in one line 
and the last half values in one line. 

Hints:

Use [n1:n2] notation to get a slice from a tuple.
'''
def tuples1():
    t = list()
    for i in range(1,11):
        t.append(i)
    print(tuple(t[:5]))
    print(tuple(t[5:]))
'''
Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 
'''
def tuples2():
    t = list()
    for i in range(1,11):
        if i%2==0:
            t.append(i)
    print(tuple(t))


















       