# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 16:54:50 2023

@author: raneja
"""

def remove_chars(s,i):
    if i<(len(s)):
        print(s[i:])
        
s=input("enter string: ")
i=int(input("enter separator: "))

remove_chars(s, i)
