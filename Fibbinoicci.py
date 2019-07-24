# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 22:08:28 2019

@author: hp
"""

x=5
n1=0
n2=1
print(n1)
print(n2)
for i in range(5):
    c=n1+n2
    n1=n2
    n2=c
    print(c)