# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 23:30:39 2018

@author: Harsh
"""

'''
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
'''
v = input("Please input here::\n\n")
num = [x for x in v.split(",") if int(x)%2!=0]
print(",".join(num))