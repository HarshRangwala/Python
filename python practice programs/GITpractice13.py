# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 22:39:05 2018

@author: Harsh
"""

'''
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''
n= input("Please input here::")
d= {"DIGITS":0, "LETTERS":0}
for c in n:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print("LETTERS::",d["LETTERS"])
print("DIGITS::",d["DIGITS"])