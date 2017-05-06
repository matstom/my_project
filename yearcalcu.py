# -*- coding: utf-8 -*-
"""
Created on Sat May  6 15:07:30 2017

@author: mats
"""

user_name = raw_input("Enter your name :")
user_age = int(raw_input("Enter your age :"))

currentyear = datetime.now().year
user_to_hun =  (currentyear - user_age) + 100
print user_to_hun
