# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:43:43 2023

@author: raneja
"""

num1, num2=map(int,input("enter numbers:").split())
# print(type(num1),type(num2))

if (num1*num2>=1000):
    print(num1+num2)
else:
    print(num1*num2)