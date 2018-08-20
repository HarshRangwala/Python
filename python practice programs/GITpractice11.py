# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 21:13:05 2018

@author: Harsh
"""

'''
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input 
and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
'''
list1=[]
items=[x for x in input("Please input here").split(",")]
divisor=int(input("set the divisiblity capacitor"))
for p in items:
    intp = int(p, 2)
    if not intp%divisor:
        list1.append(p)
        print(",".join(list1))