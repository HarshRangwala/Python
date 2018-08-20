# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 18:08:07 2018

@author: Harsh
"""
from operator import itemgetter
l = []
while True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split(",")))

print (sorted(l, key=itemgetter(0,1,2)))