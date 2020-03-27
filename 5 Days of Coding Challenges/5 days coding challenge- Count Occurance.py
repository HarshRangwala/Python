# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 18:16:52 2020

@author: Anuj
"""


s = "Wow thats a very nice price, very nice price!Really nice price I said price 4 times"
#s = "price price price price"
word_to_count = "price"
#Try1
def count_price(s):
    count = s.count("price")
    print(count)            
count_price(s)
#Try2
def count_price(s):
    word = "price"
    count = 0
    for i in range(len(s)):
        if s[i:i+len(word)] == word:
            count += 1
    return count
count_price(s)