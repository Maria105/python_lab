#!/usr/bin/env python3
# -*-coding: utf-8 -*-

a=int(input('enter a='))
b=int(input('enter b='))
c=int(input('enter c='))

h=int(input('enter height door:'))
w=int(input('enter width:'))

if h>a and w>b:
	print('fit')
elif h>b and w>a:
	print('fit')
elif h>c and w>b:
	print('fit')
elif h>b and w>c:
	print('fit')
elif h>a and w>c:
    print('fit')
elif h>c and w>a:
    print('fit')
else:
    print('not fit')
