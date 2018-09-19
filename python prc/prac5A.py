# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 20:17:44 2018

@author: Harsh
"""

d = {'1':'h','2':'a'}
j = {'3':'r','4':'s','5':'h'}
g = {'10':'r','12':'s','13':'h'}
e = d.update(j)
e = d.update(g)
print(e)
print(d)