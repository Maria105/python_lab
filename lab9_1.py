#!/usr/bin/env python3
# -*-codding:utf-8 -*-


def calculate(cards: str) -> int:
    """This function calculate your card in BlackJack """

    cards = cards.split()
    card_table = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, "K": 10,\
                  'A': 0}
    total = sum([card_table[_] for _ in cards])
    if 'A' in cards:
        ace_score = 21 - total
        if ace_score < 11:
            total = total + 1
        elif ace_score > 11:
            total = total + 11
        else:
            total = total + ace_score
    return total


def output(result: int) -> None:
    """This function output your cards or bust"""

    if result > 21:
        print("Bust")
    elif result == 21:
        print("BlackJack")
    else:
        print(result)


output(calculate(input("Enter your card")))
