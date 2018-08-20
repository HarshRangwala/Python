# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 14:36:13 2018

@author: Harsh
"""

'''
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
'''
def listing():
    l = list()
    for i in range(1,21):
        l.append(i**2)
    print(l)
'''
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
Then the function needs to print the first 5 elements in the list.

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list
'''
def listing1():
    l = list()  
    for i in range(1,21):
        l.append(i**2)
    print(l[:5])
    print(l[-5:])  #  '''Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
                   # Then the function needs to print the last 5 elements in the list.'''
'''
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
Then the function needs to print all values except the first 5 elements in the list.
'''
def listing2():
    l = list()
    for i in range(1,21):
        l.append(i**2)
    print(l[5:])
    
























