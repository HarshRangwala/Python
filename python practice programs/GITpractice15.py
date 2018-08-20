# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 23:04:05 2018

@author: Harsh
"""

'''
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''
a = int(input("Please input here::\n\n"))
a1 = int("%s" %a)
a2 = int("%s%s" %(a,a))
a3 = int("%s%s%s" %(a,a,a))
a4 = int("%s%s%s%s"%(a,a,a,a))
print("Your result is::",a1+a2+a3+a4)