#!/usr/bin/env python3
# -*-codding:utf-8 -*-


def number(number: int) -> list:
    """ This function checking your number """

    number_str = str(number)
    count = 1
    for numeric in number_str[::-1]:
        if numeric != '0':
            yield int(numeric) * count
        count *= 10


def transformation_to_roman(arabic: int) -> str:
    """This function convert to Roman number """

    roman = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI',
             7: 'VII', 8: 'VII', 9: 'IX', 10: 'X', 20: 'XX', 30: 'XXX',
             40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC',
             100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC',
             700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M', 2000: 'MM',
             3000: 'MMM'}
    return ''.join([roman.get(num) for num in number(arabic)][::-1])


def transformation_to_arabic(roman: str):
    """ This function convert to Arabic number """

    roman_num = roman_num.upper()
    keys = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM', 'I', 'V', 'X', 'L', 'C', 'D', 'M']
    arabic = {'IV': '4', 'IX': '9', 'XL': '40', 'XC': '90', 'CD': '400', 'CM': '900',
                    'I': '1', 'V': '5', 'X': '10', 'L': '50', 'C': '100', 'D': '500', 'M': '1000'}
    for key in keys:
        if key in roman_num:
            roman_num = roman_num.replace(key, ' {}'.format(arabic.get(key)))
    return sum(int(num) for num in roman_num.split())


print(transformation_to_roman(input("Enter your arabic number: ")))
print(transformation_to_arabic(input("Enter your roman number: ")))

