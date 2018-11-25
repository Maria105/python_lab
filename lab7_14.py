#!/usr/bin/env python3
# -*- codding:utf-8 -*-

def input_email() -> str:
    """Input email"""
    email = input('Enter your email: ')
    return (email)

def valid_check(email: str) -> bool:
    """Check is valid your email"""

    separation = email.split('@')[1].split('.')
    return len(separation[-1]) > 1 and email.count('@') < 2 and len(separation) > 1

print(valid_check (input_email ( ) ) )
