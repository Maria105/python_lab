#!/usr/bin/env python3
# -*- codding:utf-8 -*-

def input_text() -> str:
    """Input message: """
    text = input('enter you text: ')
    return (text)

def remove_spaces(text: str) -> str:
    """Remove all unnecessary spaces from the string"""
    return ' '.join (text.split())

print(remove_spaces(input_text()))
