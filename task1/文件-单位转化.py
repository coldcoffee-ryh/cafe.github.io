#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 14:59:15 2021

@author: ryh
"""
sum=0.00
with open('in162.txt','r') as f1:
   t=f1.readline()
   q=t.split()
for i in q:
   sum+=float(i)*0.454
with open('out162.txt','w+') as f2:
    f2.write(str(sum))
for line in f2:
    print(line)
f1.close()
f2.close()
    
