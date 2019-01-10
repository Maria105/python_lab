#!/usr/bin/env python3
# -*- codding:utf-8 -*-

def selection_sort(source: list) -> list:
    """Sort your list """

    for i in range(len(source)):
        min_i = min(source[i:])
        min_index = source[i:].index(min_i)
        source[i + min_index] = source[i]
        source[i] = min_i
    return source


print(selection_sort([6, 7, 4, 117, 9, 7, 56, 0, 1, 2]))
