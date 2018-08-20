# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 17:40:35 2018

@author: Harsh
"""

char = str(input("Please input here!"))
def isvowel(char):
    return False if 'a,e,i,o,u,A,E,I,O,U'.find(char) < 0 else True
print(isvowel(char))