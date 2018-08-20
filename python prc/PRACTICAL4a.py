# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 17:58:36 2018

@author: Harsh
"""

def commlist(list1,list2):
    for x in list1:
        for y in list2:
            if x==y:
                return True
print(commlist([1,2,3,4,5], [5,6,7,8,9]))