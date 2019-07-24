# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 14:18:55 2019

@author: hp
"""

inp = input('Enter Fahrenheit Temperature: ')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
    
except:
    print('Enter a valid number')