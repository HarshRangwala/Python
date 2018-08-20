# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 15:29:18 2018

@author: Harsh
"""

'''
Write a program that accepts sequence of lines as input
and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''
l=[]    #List l createdf
while True:
    s=input("Please input here")  # input a line 
    if s:
        l.append(s.upper()) #converts a line to uppercase
    else:
        break #loops out
    for sent in l: 
        print(sent)
        