#!/usr/bin/env python3
#-*-coding: utf-8 -*-

import math

a=float(input('enter number a:'))
b=float(input('enter number b:'))
c=float(input('enter number c:'))
e=math.exp
p=math.pi

f=1/(c*math.sqrt(2*p))*e(-((a-b)**2)/2*(c**2))
print(f)
