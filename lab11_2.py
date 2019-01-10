#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def create_initial_value(seed: str) -> int:
    if len(seed) < 6:
        seed = '0' * (6-len(seed)) + seed
    elif len(seed) > 6:
        raise ValueError('Error')

    while True:
        seed = str(seed)
        current_value = list(str(int(seed[3:] + seed[0:3]) * int(seed)))
        while len(current_value) > 7: 
            current_value.pop(0); current_value.pop(-1)
        if len(current_value) > 6: 
            del current_value[-1]
        seed = int(''.join(current_value))
        yield seed

a = create_initial_value(input("Input seed: "))
print(a.__next__())
print(a.__next__())
print(a.__next__())

