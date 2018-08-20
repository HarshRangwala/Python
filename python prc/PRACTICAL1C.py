# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 17:45:10 2018

@author: Harsh
"""
nterms = int(input("Enter the number of terms"))
n1 = 0
n2 = 1
count = 0

if nterms<0:
    print("Please enter a positive number")
elif nterms == 1:
    print("Fibonacci Sequence upto :",nterms)
    print(n1)
else:
    print("Fibonacci Sequence upto :",nterms)
    while count<nterms:
        print(n1)
        nth = n1+n2
        #UPDATE THE VALUES
        n1=n2
        n2=nth
        count+=1
