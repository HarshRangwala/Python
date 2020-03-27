# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 13:41:09 2020

@author: Anuj
"""

string = input("Your value here: ")
list=[hex(ord(ch)) for ch in string]
print(tuple(list))
