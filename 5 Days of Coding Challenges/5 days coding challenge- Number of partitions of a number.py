# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 17:38:53 2020

@author: Anuj
"""

n = int(input("Enter the number : "))
partitions = []
def compositions(remainder, start = 1):
    if remainder == 0:
        print(" + ".join(partitions),"=", n)
    else:
        for add in range(start, remainder + 1):
            partitions.append(str(add))
            compositions(remainder - add, add)
            partitions.pop()
compositions(n)