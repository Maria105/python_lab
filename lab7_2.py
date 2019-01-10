#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def output() -> str:
    phrase = str(input ('enter you phrase: '))
    return (phrase)

def process_phrase ( phrase: str ):
    phrase = phrase.lower()
    forbiddeb = (' ', '.', '?', '!', ':', ';', '-', ',', " ' " )
    for i in forbiddeb:
        phrase = phrase.replace(i, ' ')
    return phrase

def audit ( phrase: str):
    a = phrase[::-1]
    if phrase == a:
        print('True')
    else:
        print('False')

print ( audit ( process_phrase (output() ) ) )
