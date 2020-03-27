# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 12:14:00 2020

@author: Anuj
"""
num1 = input("Number: \n")
num2 = input("Number: \n")

def decimalToBinary(num, k_prec) : 
    binary = ""  
    Integral = int(num)    
    fractional = num - Integral  
    while (Integral) :           
        rem = Integral % 2
        binary += str(rem);    
        Integral //= 2
    binary = binary[ : : -1]  
    binary += '.'
    while (k_prec) :           
        # Find next bit in fraction  
        fractional *= 2
        fract_bit = int(fractional)    
        if (fract_bit == 1) :               
            fractional -= fract_bit  
            binary += '1'              
        else : 
            binary += '0'  
        k_prec -= 1  
    return binary 
def binary_addition(num1, num2):
    if num1.isdigit() or num2.isdigit():
        num1 = str(num1)
        num2 = str(num2)
        return "binary addition is: ", bin(int(num1, 2)+int(num2, 2))
    else:
        var1 = str(num1).split('.')
        var2 = str(num2).split('.')
        number1 = int(var1[0], 2)+ int(var1[1], 2)/2.**len(var1[1])
        #print(number1)
        number2 = int(var2[0], 2)+ int(var2[1], 2)/2.**len(var2[1])
        #print(number2)
        v = number1+number2
        return "Binary addition is: ",decimalToBinary(v, 3)
print(binary_addition(num1, num2))

'''
binary1, binary2 = input().split(' ')
N = int(binary1, 2)
M = int(binary2, 2)
print(' ', N, M)
'''
















