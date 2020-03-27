# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:02:45 2020

@author: Anuj
"""
import re
def to_upper(match):
    return match.group(1).upper()

s = str(input("Enter a string that contains at least one - caps lock :\n"))
out = re.sub(r'\bcaps lock (\S+)', to_upper, s.lower())
print(out)

        
        
        
            