# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 19:58:32 2023

@author: raneja
"""

def exponent(base, exp):
    return base**exp

base, exp=map(int,input('enter base and expo: ').split())
result=exponent(base, exp)

print(result)