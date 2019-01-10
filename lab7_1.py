#!usr/bin/env pyhton3
#-*- codding: utf-8 -*-

def input_datas() ->list:
    """This function input datas"""

    line = input('Enter line: ')
    number = int(input('Enter number: '))
    return [line, number]

def shift_line(string: list) ->str:
    """This function shift your line"""

    first_line = string[0][0: string[1]]
    second_line = string[0][string[1]:]
    new_line = second_line + first_line
    return(new_line)

def output(new_line: str) -> str:
    """This function output dara"""

    print(new_line)

output(shift_line(input_datas()))

