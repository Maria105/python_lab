#!/usr/bin/env python3
# -*- codding:utf-8 -*-

def input_text() -> str:
    """Input message: """
    text = input('enter you text: ')
    return (text)
def sort_words(text: str) -> str:
    """Sort words in a row to increase their length"""
    return ' '.join(sorted (text.split( ), key=len ) )

print (sort_words (input_text ( ) ) )
