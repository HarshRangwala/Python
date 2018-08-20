# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 14:51:25 2018

@author: Harsh
"""
'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''
class InputOutString(object):

    def getString(self):
        self.s = input("Please input here::")

    def printString(self):
        print (self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()