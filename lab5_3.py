#!/usr/bin/env python3
#-*-coding: utf-8 -*-

import random
user_choice=input('choose stone, paper or scissor: ')
computer_choice=random.choice(['stone', 'paper', 'scissor'])

print (computer_choice)
if user_choice == computer_choice:
    print("So it's a tie")

elif user_choice == 'stone':
    if computer_choice == 'paper':
        print ('you loose')
    elif computer_choice == 'scissor':
        print ('you won')
elif user_choice == 'paper':
    if computer_choice == 'stone':
        print ('you won')
    elif computer_choice == 'scissor':
        print ('you loose')
elif user_choise == 'scissor':
    if computer_choice == 'stone':
        print ('you loose')
    elif cmputer_choice == 'paper':
        print ('you won')

