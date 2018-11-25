#!/usr/bin/env python3
#-*- codding: utf-8 -*-

def input_text() -> str:
    """Enter text"""
    text = input('Enter text in English: ')
    return (text)

def return_vowel(text: str) -> str:
    """Find and return vowel letters"""
    vowels = text.count('a') + text.count('o') + text.count('u') +\
    text.count('i') + text.count('e') + text.count("y") +\
    text.count('A') + text.count('O') + text.count('U') +\
    text.count('I') + text.count('E') + text.count('Y')
    return (vowels)

def output(vowels: str) -> str:
    """Output vowels letter"""
    print (vowels)
output( return_vowel ( input ( ) ) )
