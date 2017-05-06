# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 18:45:11 2017

@author: mats
"""
#pi = 3.14
#radius = 2.2
#area = pi*(radius**2)
#print(area )
#radius = radius + 1
#area = pi*(radius**2)
#print(area)

#num = int(raw_input("type a number ..."))
#print(5*num)

s = 'demo loops'
#for index in range(len(s)):
#   if s[index] == "i" or s[index] == "u":
#        print ('there is an i or u')
#else:
#   print("no i or u")
for char in s:
    if char == 'i' or char == 'u':
        print('there is an i or u')