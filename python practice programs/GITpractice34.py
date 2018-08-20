# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 18:18:30 2018

@author: Harsh
"""
'''
Write a program which can filter even numbers in a list by using filter function.
The list is: [1,2,3,4,5,6,7,8,9,10].
'''
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter(lambda x: x%2==0, li)
print(evenNumbers)