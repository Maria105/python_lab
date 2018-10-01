#!/usr/bin/env python3

def input_sides() -> list:
    """This function takes three sides of triangle"""

    a = int(input('enter first side a: '))
    b = int(input('enter second side b: '))
    c = int(input('enter third side c: '))

    return [a, b, c]

def  calculate_area(lst: list) -> float:
    """This function calculation area of triangle"""


    p = (lst[0] + lst[1] + lst[2]) / 2
    s =  ( p * ( p - lst[0] ) * ( p - lst[1] ) * ( p - lst[2] ) )** 0.5
    return (s)

def output_area(s: float) -> float:
    print('area of triangle', s )

output_area ( calculate_area ( input_sides ( ) ) )
