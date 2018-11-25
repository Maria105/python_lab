#!/usr/bin/env python3
# -*- codding:utf-8 -*-

def input_text() -> str:
    """Input message: """
    text = input('enter you text: ')
    return (text)

def min_word(text: str) -> str:
    """Find smallest word"""

    return min(text.split())

print(min_word(input_text()))
