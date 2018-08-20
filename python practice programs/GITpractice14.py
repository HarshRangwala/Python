# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 22:57:01 2018

@author: Harsh
"""

'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''
n = input("Please input here::")
d={"UPPER":0, "LOWER":0}
for c in n:
    if c.isupper():
        d["UPPER"]+=1
    elif c.islower():
        d["LOWER"]+=1
    else:
        pass
print("UPPER CASE LETTERS::>\n\n", d["UPPER"])
print("LOWER CASE LETTERS::>\n\n", d["LOWER"])