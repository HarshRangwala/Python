# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 20:23:02 2018

@author: Harsh
"""

'''
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
'''
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print (evenNumbers)