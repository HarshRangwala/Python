# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 16:27:55 2018

@author: Harsh
"""

list1 =[]
list2 = (input("Please input the number here::").split(","))
list1.extend(list2)
print(list1)
list3=[]
for i in reversed(list1):
    print(i)