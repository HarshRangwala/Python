# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 23:12:36 2020

@author: Anuj
"""
#s = "BANANAS"
def vowel_check(s):
    list_of_vowel = ["a","e","i","o","u"]
    s = s.lower()
    i = 0
    if s[0].lower() in list_of_vowel or s[len(s)-1:] in list_of_vowel:
        return False
    else:
        for letter in s:
            if i%2 == 0:
                if str(s[i]).lower() in list_of_vowel:
                    return False
                else:
                    pass
            else:
                if str(s[i]).lower() in list_of_vowel:
                    return True
                return False
            i = i + 1
print(vowel_check("BANANAS"))
print(vowel_check("AXE"))