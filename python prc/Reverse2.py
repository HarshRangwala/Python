# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 15:55:30 2018

@author: Harsh
"""

# function which return reverse of a string
def reverse(s):
	return s[::-1]
s= str(input("Please Input Here::\n\n"))
print("The reversed outcome of",s,"is ::\n\n",reverse(s))