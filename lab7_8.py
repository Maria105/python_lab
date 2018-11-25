#!/usr/bin/env python3
# -*- codding: utf-8 -*-

def FizzBuzz() -> str:
    """Multiplicity check for three or five"""
    return [(not n % 3) * 'Fizz' + (not n % 5) * 'Buzz' or n for n in range(1, 101)]

print(FizzBuzz())
