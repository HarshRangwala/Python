# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 18:00:19 2018

@author: Harsh
"""

num = int(input("Please Enter the your number"))
rev=0
while(num>0):
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
print("The reverse outcome of the number you entered is :: %d" %rev)