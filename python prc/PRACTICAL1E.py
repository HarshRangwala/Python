# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 18:26:47 2018

@author: Harsh
"""
def Armstrong():
    num=int(input("Please Input here::"))
    # initialize sum
    sum = 0
    # find the sum of the cube of each digit
    temp = num
    while temp > 0:
           digit = temp % 10
           sum += digit ** 3
           temp //= 10
           # display the result
           if num == sum:
               print(num,"is an Armstrong number")
           else:
               print(num,"is not an Armstrong number")
              
def pallindrome1():
    num=int(input("Please Input here::"))
    sum1=0
    n=num
    while num!=0:
        rem=num%10
        sum1=(sum1*10)+rem
        num=num//10
        if sum1==n:
            print(n,"is a palindrome")
        else:
            print(n,"is not a palindrome number")
Options={
        0: Armstrong,
        1: pallindrome1
        }
Selection = 0
while Selection != 2:
    print("0. Armstrong")
    print("1. Pallindrome1")
    Selection = int(input("Select an option: "))
    if (Selection >= 0) and (Selection < 2):
        Options[Selection]()