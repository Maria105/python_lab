#!/usr/bin/env python3
#-*- coding: utf-8 -*-


a=int(input('enter first side of triangle: '))
b=int(input('enter second side of triangle: '))
c=int(input('enter fird side of triangle: '))

if  a<=0 or b<=0 or c<=0:
    print('triangle does not exist')
elif a+b>c and b+c>a and a+c>b:
    print('triangle exists')
else:
    print('triangle does not exist')
