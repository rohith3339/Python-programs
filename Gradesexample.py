# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 15:14:24 2019

@author: hp
"""

x=input('Enter the score')
try:

    x=float(x)
    if(0.0<x<1.0):
        if (x>=0.9):
            print('A')
        elif (x>=0.8):
            print('B')
        elif (x>0.7):
            print('C')
        elif (x>=0.6):
            print('D')
        elif(x<0.6):
            print('F')
    else:
        print('Badscore')
except:
    print('Enter a valid score')

