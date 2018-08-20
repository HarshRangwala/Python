# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 15:20:23 2018

@author: Harsh
"""

'''
Write a program that accepts a comma separated sequence of words as 
input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''
items=[y for y in input().split(',')]
items.sort()
print(','.join(items))