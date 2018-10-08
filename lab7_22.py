#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def process_phrase ( text: str ):
    text = text.lower()
    forbiddeb = (' ', '.', '?', '!', ':', ';', '-', ',', " ' " )
    for i in forbidden:
        text = text.replase(i, '' )
    return text
def reverse ( text: str):
    a = text[::-1]
    retirn (a)
def is_palindrome(text):
    new = process_text(text)
    return process_text ( text ) == reverse ( process_text ( text ) )
phrase = input ( 'enter your text' )
if (is_palindrome ( phrase ) ):
    print('True')
else:
    print('False')

