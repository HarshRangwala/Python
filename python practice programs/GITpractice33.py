# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 17:17:30 2018

@author: Harsh
"""

'''
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 
'''
accstr = str(input("Please input here::"))
def inpstr(accstr):
    if (accstr == 'yes') or (accstr == 'YES') or (accstr == 'Yes'):
        return 'Yes'
    else:
        return False
print(inpstr(accstr))