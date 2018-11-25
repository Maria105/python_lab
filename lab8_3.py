#!/usr/bin/env python3
# -*- codding:utf-8 -*-


import functools


def average(source: list) -> float:
    """This function search average value """

    return functools.reduce((lambda x, y: x + y), source) / len(source)


def median(source: list) -> float:
    """This function search median """

    number = len(source)
    if len(source) % 2 == 1:
        return sorted(source)[number//2]
    else:
        return sum(sorted(source)[number//2-1:number//2+1])/2


print(average([5, 7, 1, 2, 4, 3, 6, 5]))
print(median([8, 7, 3, 1, 2, 4, 8, 5]))
