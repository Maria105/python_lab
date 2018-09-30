#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

a=float(input('enter a>=0: '))

b=float(input('enter b>0: '))

e=math.e

x=math.sqrt(a*b)/(math.exp(a)*b)+a*math.exp(2*a/b)
print(x)
