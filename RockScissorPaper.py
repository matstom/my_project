# -*- coding: utf-8 -*-
"""
Created on Mon May 15 18:01:26 2017

@author: mats
"""

import random 

#user1 = raw_input('Enter name : ')
#user2 = raw_input('Enter name : ')

opt = ('R', 'P', 'S')
print "R : Rock, P : Paper, S : Scissors"

u1 =0
u2 =0

while True:
    player1 = raw_input('Enter your choice :').upper()
    print player1
#player2 = raw_input('Enter your choice :').upper()
    player2 = random.choice(opt)
    print player2
   
    if player1 == player2:
        #print 'Both players input same value , hence a tie'
        pass
    elif player1 == 'R' and player2 ==  'S':
        print ' Rock beats scissors'
        u1 = u1 +1
    elif player1 == 'R' and player2 ==  'P':
        print ' Paper covers Rock'
        u2 = u2+1
    elif player1 == 'S' and player2 ==  'R':
        print ' Rock beat Scissors'
        u2 = u2+1
    elif player1 == 'S' and player2 ==  'P':
        print ' Scissor cuts Paper'
        u1 = u1+1
    elif player1 == 'P' and player2 ==  'S': 
        print ' Rock beats Scissor'
        u1 = u1 +1
    elif player1 == 'P' and player2 ==  'R':
        print ' Paper covers Rock'
        u2 = u2+1
    
    if u2 == 2:
        print 'Player2 won the game '
        break
    elif u1 == 2: 
        print 'Player1 won the game'
        break