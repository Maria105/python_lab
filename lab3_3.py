#!/usr/bin/env python3
#-*- coding: utf-8 -*-

weight=float(input(' введіть власну вагу в кілограмах:'))
height=float(input('введіть власний зріст в метрах: '))

Body_mass_index=weight/height**2
print('Ваш індекс маси тіла: ' + str(Body_mass_index) )
