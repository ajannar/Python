# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 15:56:11 2023

@author: raneja
"""

lst=[1,2,3,4,5,6,7,8,9,0]

num=0

for i in range(len(lst)):
    print('previous number: ',num)
    print('current number: ',lst[i])
    print('sum: ',(num+lst[i]),'\n')
    num=lst[i]