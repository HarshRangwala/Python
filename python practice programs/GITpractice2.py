# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 18:21:30 2018

@author: Harsh
"""

'''The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320 '''
def fact(x):
    if x==0:
        return 1
    return x*fact(x-1)
x= int(input("Please Input Here::"))
print(fact(x))