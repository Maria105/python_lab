#!/usr/bin/env python3
# -*- codding:utf-8 -*-


def killing_third(number: int) -> int:
    """This function kills every third person """

    lst = list(range(1, number + 1))
    count = 0
    while len(lst) > 1:
        first = lst.pop(0)
        if count % 3:
            lst.append(first)
            count = 0
        else:
            count += 1
    return lst

print(killing_third(10))
