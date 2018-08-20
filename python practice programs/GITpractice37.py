# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 18:29:37 2018

@author: Harsh
"""

'''
Define a class named American which has a static method called printNationality.
'''
class American:
    @staticmethod
    def printNationality():
        print("American")
American.printNationality()
'''
Define a class named American and its subclass NewYorker. 
'''
class American(object):
    pass
class NewYorker(American):
    pass
anAmerican = American()
aNewYorker = NewYorker()
print(anAmerican())
print(aNewYorker())