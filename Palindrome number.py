# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 21:55:45 2019

@author: hp
"""

x=input('Enter the number')
x=int(x)
v=x
r=0
while(x>0):
    b=x%10
    r=r*10+b
    x=x//10
if (v==r):
    print('number is palindrome')
else:
    print('number is not palindrome')
    

    