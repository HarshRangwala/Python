# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 13:31:05 2018

@author: Harsh
"""
num = int(input("Please input here::"))
def sqr(num):
    if num <= 0:
        return False
    return num**2
print(sqr(num))