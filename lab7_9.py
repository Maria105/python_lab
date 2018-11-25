#!/usr/bin/env python3
# -*- codding:utf-8 -*-



def check_ticket(number: str) -> bool:
    """Check is ticket lucky"""
    half_ticket = int(len(number) / 2 )
    first_half = list(map(int, number[0: half_ticket]))
    second_half = list(map(int, number[-half_ticket :]))
    return sum(first_half) == sum(second_half)

print(check_ticket(input("Input number ticket: ")))
