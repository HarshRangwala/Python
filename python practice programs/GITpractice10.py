# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 15:42:55 2018

@author: Harsh
"""

'''
Write a program that accepts a sequence of whitespace separated words as 
input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''
s= input("Please input here::\n\n\n\n\n\n")
w= [x for x in s.split(" ")] #s.split accepts only sentence with no comma only a seperator
print(" ".join(sorted(list(set(w)))))

