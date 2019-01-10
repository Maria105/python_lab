#!/usr/bin/env python3
#-*-coding: utf-8 -*-

import decimal

wage = decimal.Decimal(input('Input your wage: '))
income_individual = decimal.Decimal('0.18')
military_tax = decimal.Decimal('0.015')

all_summ = str(wage * (income_individual + military_tax))

print ('Amount of taxes: ' + all_summ )
