#!/usr/bin/env python3
#-*- cpdding: utf-8 -*-

def input_text() -> str:
    """Input needed two text"""
    text_1 = input('Enter first text: ')
    text_2 = input('Enter second text: ')
    return [text_1, text_2]

def check(text_1, text_2: str) -> bool:
    """Check is anagram two text"""

    return not[0 for _ in text_1 if text_1.count(_) > text_2.count(_)]

print(check (input_text ( ) ) )
