#!/usr/bin/env python3
#-*- codding: utf-8 -*-

def input_text() ->str:
    """Enter needed text"""
    text = input('Enter text: ')
    return (text)

def substitution_stars(text: str) ->str:
    """Create border"""
    print ('*' * len(text) +'****\n'+"*", text, "*\n"+'*' * len(text) + '****' )

substitution_stars (input_text ( ) )
