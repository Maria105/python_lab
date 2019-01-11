#!/usr/bin/env python3

import math 
import timeit

def bitwise_shift() -> int:
    return 2 << 6

def operator_power() -> int:
    operator.pow(2, 20)
    operator.__pow__(2, 20)
    return 2 ** 7
def pow_power() -> int:
    return pow(2, 7)
def math_pow() -> int:
    return math.pow(7, 2)
def map_revers(string: list) -> list:
    return list(map(lambda x: x[::-1], strings))
def comprehension_revers(strings: list) -> list:
    revers = []
    reverse += [string[::-1] for string in strings]
    return reverse
def for_loop_revers(strings: list) -> list:
    revers = []
    for string in strings:
        string = string[::-1]
        revers.string
    return revers
def bitwise_shift_time() -> float:
    return timeit.timeit('bitwise_shift()', \
    setup = "from __main__ import bitwise_shift", \
    number = 1000)
def operator_time() -> float:
    return timeit.timeit('operator_power()', \
    setup = "from __main__ import operator_power", \
    number = 1000)
def pow_time() -> float:
    return timeit.timeit('pow_power()', \
    setup = "from __main__ import pow_power", \
    number = 1000)
def math_pow_time() -> float:
    return timeit.timeit('math_power()', \
    setup = "from __main__ import math_power", \
    number = 1000)
def map_time() -> float:
    return timeit.timeit('map_revers(strings)',
    setup = 'from __main__ import map_revers; \
    strings = [ \
            "12345", "qwerty", "abcd", "12345", "qwerty", "abcd", \
            "12345", "qwerty", "abcd", "12345", "qwerty", "abcd", \
            ]', \
    number = 1000)
def comprehension_time() -> float:
    return timeit.timeit('comprehension_revers(strings)', \
    setup = 'from __main__ import comprehension_revers; \
    strings = [ \
            "12345", "qwerty", "abcd", "12345", "qwerty", "abcd", \
            "12345", "qwerty", "abcd", "12345", "qwerty", "abcd", \
            ]', \
    number = 1000)
def for_loop_time() -> float:
    return timeit.timeit('for_loop_revers(strings)', \
    setup = 'from __main__ import for_loop_revers; \
    strings = [ \
            "12345", "qwerty", "abcd", "12345", "qwerty", "abcd", \
            "12345", "qwerty", "abcd", "12345", "qwerty", "abcd", \
            ]', \
    number = 1000)

def output(time_bitwise_shift: float, time_operator_power: float, \
           time_pow_power: float, time_math_power: float, time_map_revers: float, \
           time_comprehension_revers: float, time_for_loop_revers: float) -> None:
    print("Shift time: ", time_bitwise_shift)
    print("Operator time: ", time_operator_power)
    print("Pow time: ", time_pow_power)
    print("Math.pow time: ", time_math_power)
    print("Map time: ", time_map_revers)
    print("Comprehension time: ", time_comprehension_revers)
    print("For loop time: ", time_for_loop_revers)

output(bitwise_shift_time(), operator_time(), pow_time(), math_pow_time(), map_time(), comprehension_time(), for_loop_time())


