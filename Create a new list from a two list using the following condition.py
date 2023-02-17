# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 18:14:12 2023

@author: raneja
"""

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

list3=[]

for i in range(len(list1)):
    if list1[i]%2!=0:
        list3.append(list1[i])
        
for i in range(len(list2)):
    if list2[i]%2==0:
        list3.append(list2[i])
        
print(list3)