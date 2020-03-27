# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 03:44:28 2020

@author: Anuj
"""
def sumsq(l):
    l.sort()
    m = 0
    for i in range(len(l) - 2):
        for j in range(m +1,len(l)):
            for m in range(i+1, len(l)-1):
                x = l[i]*l[i]
                y = l[j]*l[j]
                z = l[m]*l[m]
    if y == x+z:
        return True
    return False
                
print(sumsq([4, 3, 5]))
print(sumsq([7, 12, 14]))
