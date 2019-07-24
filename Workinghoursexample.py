# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 14:51:46 2019

@author: hp
"""
hours=input('Enter the employee working hours')
try:
    hours=int(hours)
    rate= 10
    
    if (hours>40):
        rate=rate*1.5
        pay=hours*rate
        print(pay)
    elif(hours<0):
        print('employee leaves before working hours')
    else:
        pay=hours*rate
        print(pay)
except:
    print('Enter valid working days')