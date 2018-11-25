#!/usr/bin/env python3

import math
import decimal

def input_datas() -> list:
    """This function takes datas about you deposit"""

    a = decimal.Decimal(input('enter your summ: '))
    b = decimal.Decimal(input('enter annual interest rate in percent: '))
    c = decimal.Decimal(input('enter final amount: '))

    return [a, b, c]

def calculate_duration (lst: list) -> float:
    """Calculate duration """

    duration =  math.log ( lst[2] / lst[0] , (1 + lst[1] / 100 ) )
    return duration

def output_duration ( years: float ) -> float:
    print ('Number of years: ', years)

output_duration ( calculate_duration ( input_datas ( ) ) )
