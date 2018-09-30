#!/usr/bin/env python3
#-*- coding: utf-8 -*-

a=int(input('enter number a>0: '))
if a > 1:
    i = 2
    while i!=int(a**0.5)+1:
        if (a % i) == 0:
            print('not simple number')
            break
        i += 1
    else:
        print('simple number')
else:
    print('not simple number')
