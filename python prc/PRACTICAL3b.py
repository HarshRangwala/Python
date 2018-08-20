# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 17:52:26 2018

@author: Harsh
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newa=[]
for nums in a:
    if nums<5:
        newa.append(nums)
print(newa)        