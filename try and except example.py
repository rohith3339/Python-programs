# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 15:07:51 2019

@author: hp
"""
hours=input('Enter no:of sick hours')
rate=input('Enter the amount per hour')
try:
    hours=int(hours)
    rate=float(rate)
    pay=hours*rate
    print(pay)
except:
    print('Enter valid input')
    
