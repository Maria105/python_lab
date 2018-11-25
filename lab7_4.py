#!/usr/bin/env python3
# -*- cpdding-8 -*-

def input_datas() -> str:
    """Input messaege"""
    message = input('Enter your message: ')
    return message

def codding(message: str) -> str:
    """Codding the message"""
    codding = list ( map (lambda x: chr (ord (x) + 1 ), message ) )
    return ''.join (codding)

def output(codding: str) -> str:
    """Output codding message"""
    print(codding)

output ( codding ( input_datas ( ) ) )
