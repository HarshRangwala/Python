# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 20:20:06 2018

@author: Harsh
"""

'''
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
'''
li = [1,2,3,4,5,6,7,8,9,10]
sqnum = map(lambda x: x**2, li)
print(sqnum)