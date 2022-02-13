#!/usr/bin/env python
# file <calc>

# BEGIN

import random

WHAT_TO_GO = 'What is the result of the expression?'


def complete_the_game(number):
    number = int(abs(random.randint(1, 100)))
    x = random.randrange(1, number, 1)
    y = random.randrange(1, number, 1)
    arifmetic = random.randrange(1, 4, 1)
    if arifmetic == 1:
        the_task = str(x) + ' + ' + str(y)
        correct_answer = str(x + y)
        return the_task, correct_answer
    if arifmetic == 2:
        the_task = str(x) + ' - ' + str(y)
        correct_answer = str(x - y)
        return the_task, correct_answer
    if arifmetic == 3:
        the_task = str(x) + ' * ' + str(y)
        correct_answer = str(x * y)
        return the_task, correct_answer

# END
