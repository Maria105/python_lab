#!/usr/bin/env pyhton3
# -*- codding: utf-8 -*-

def input_datas() -> str:
    """This function input datas"""
    expression = input("Enter your expression")
    return(expression)

def check_possitions(expression: str) -> str:
    """This function check the correct possitioning of the brackets"""
    open = tuple('({[')
    close = tuple(')}]')
    mapping = dict(zip(open, close))
    queue = []

    for letter in expression:
        if letter in open:
            queue.append(mapping[letter])
        elif letter in close:
            if not queue or letter!= queue.pop():
                print(False)

def output(queue: list) -> list:P
    """This function output queue"""
    print (not queue)

output()
