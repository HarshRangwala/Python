# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 14:41:25 2020

@author: Anuj
"""


n= 405
def sum_cubes (n,k):
    while(k):
        st = 0
        for i in str(n):
            num = int(i)**3
            st += num
        n = st
        k = k-1
    return st
print(sum_cubes(n, 5))