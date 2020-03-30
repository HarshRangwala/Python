# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 12:12:16 2020

@author: Anuj
"""

from math import sqrt
l, l1 = list(), list()
t = 139
tup = list()
for i in range(0, len(str(t))):
    #print(str(t)[i:len(str(t))])
    tup.append(int(str(t)[i:len(str(t))]))
v = tuple(tup)
print(v)
from math import sqrt
from itertools import count, islice

def is_prime(n):
    if n < 2:
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True
for i in v:
    if is_prime(i) == True:
        l.append(i)
    if is_prime(i) == False:
        l1.append(i)
print(tuple(l),"are prime")
print(tuple(l1),"are not prime")