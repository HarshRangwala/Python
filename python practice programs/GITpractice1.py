# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 18:13:26 2018

@author: Harsh
"""

'''Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
   between 2000 and 3200 (both included).
   The numbers obtained should be printed in a comma-separated sequence on a single line.'''
H=[]
for i in range(2000,3200):
    if (i%7) and (i%5!=0):
        H.append(str(i))
print(",".join(H))