# -*- coding: utf-8 -*-
"""
Created on Mon May 15 19:44:26 2017

@author: mats
"""

import random


guess = 0
count = 0

while True:
    num = random.randint(1,9)
    print num
    guess = raw_input('Choose your guess :')
    if guess == 'exit':
        break
    guess = int(guess)
    count +=1
    if guess>num:
        print 'Guess too high'
    elif guess<num:
        print 'Guess too low'
    else:
        print 'Exact guess'
        print 'it takes',count,'times for exact guess'
        break