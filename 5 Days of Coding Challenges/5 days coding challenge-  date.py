# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 13:30:41 2020

@author: Anuj
"""
#Problem 2 A
dicti = {'01':13,'02':14,'03':15,'04':16,'05':17,'06':18,'07':19,'08':20,'09':21,'10':22,'11':23,'12':12}
s = '08:26PM'
if s.endswith('AM'):
    if s.startswith('12'):
        s1=s[:8]
        bb=s1.replace('12','00')
        print (bb)
    else:
        s1=s[:5]
        print(s1)
else:
    s1=s[:8]
    time= str(s[:2])
    ora=str(dicti[time])
    aa=s1.replace(time,ora)
    print(aa[:5])

#Problem 2 B
from datetime import date
date_entry = input('Enter a date in YYYY-MM-DD format')
year, month, day = map(int, date_entry.split('-'))
input_date = date(year, month, day)
delta = date(input_date.year, 12, 31) - input_date
print( delta.days+1)