# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 17:19:31 2018

@author: Harsh
"""
def panagram(nt):
    checkin = "abcdefghijklmnopqrstuvwxyz"
    for i in checkin:
        if(i in nt):
            continue
        else:
            return False
    return True
n=input("Please input here::")
if(panagram(n.lower())):
    print("PANAGRAM")
else:
    print("~PANAGRAM") 