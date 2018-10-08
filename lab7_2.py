#!/usr/bin/env python3
#-*- coding: utf-8 -*-

phrase = str(input ('enter you phrase: '))

def process_phrase ( phrase: str ):
    phrase = phrase.lower()
    forbiddeb = (' ', '.', '?', '!', ':', ';', '-', ',', " ' " )
    for i in forbidden:
        phrase = phrase.replase(i, ' ' )
    return phrase

def audit ( phrase: str):
    a = phrase[::-1]
    if phrase == a:
        print('True')
    else:
        print('False')
print ( audit ( process_phrase ( ) ) )
