# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 14:41:50 2020

@author: Anuj
"""

l = list()
for i in range(1, 42):
    l.append(i)
#listOfNum = [elem for elem in l if elem%3!=0]
#print(listOfNum)

def kill_soldiers(int_list):
    #list starts with 0 index
    position = 3 - 1 
    idx = 0
    len_list = (len(int_list))
    while len_list>1:
        idx = (position+idx)%len_list
        int_list.pop(idx)
        len_list -= 1
    return int_list[0]
    
print(kill_soldiers(l), "is the position where you'll save")