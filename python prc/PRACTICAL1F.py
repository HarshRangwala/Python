# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 21:57:09 2018

@author: Harsh
"""

def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
num=int(input("Please Input Here"))
if num<0:
    print("Sorry,only positive numbers accepted")
elif num==0:
        print("The factorial of 0 is 1!")
else:
    print("The factorial of",num,"is",fact(num))
print("Hello sir we are here now. shall we")