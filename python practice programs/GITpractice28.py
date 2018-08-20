# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 14:57:08 2018

@author: Harsh
"""

def printValue(n):
	print (str(n))

print(printValue(3))
'''
Define a function that can accept two strings as input and print the string with maximum length in console. 
If two strings have the same length, then the function should print al l strings line by line.

Hints:

Use len() function to get the length of a string
'''
def getstring():
    str1,str2 = [str(x) for x in input("Please input here::").split(",")]
    if len(str1)>len(str2):
        print(str1)
    elif len(str2)>len(str1):
        print(str2)
    else:
        print("All strings are of same length")
        print(str1)
        print(str2)        