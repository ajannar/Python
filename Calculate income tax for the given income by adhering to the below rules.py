# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 18:50:15 2023

@author: raneja
"""

income=int(input('enter income: '))

tax=0

    
if income<20000 and income>10000:
    tax=tax + 10000*0.10

if (income>20000):
    tax= tax+(income-20000)*0.20 + 10000*0.10
    
print(tax)
    