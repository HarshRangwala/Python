# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 13:39:19 2018

@author: Harsh
"""

'''
Python has many built-in functions, and if you do not know how to use it, 
you can read document online or find some books. 
But Python has a built-in document function for every built-in functions.
Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
And add document for your own function
'''
print(abs.__doc__)

'''
 Define a class, which have a class parameter and have a same instance parameter.
'''
'''
Define a function with two numbers as arguments. You can compute the sum in the function and return the value.
'''
num1,num2 = [int(x) for x in input("Please input here::\n").split(",")]
def sumation(num1,num2):
    if (num1<=0) and (num2<=0):
        return False
    return num1+num2
print("\n\t\n\t>>",sumation(num1,num2),"<<\t\n\t\n")