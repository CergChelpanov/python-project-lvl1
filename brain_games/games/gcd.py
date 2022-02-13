#!/usr/bin/evn python
# file <gcd>

# BEGIN

import random

WHAT_TO_GO = 'Find the greatest common divisor of given numbers.'


def complete_the_game(number):
    x = random.randrange(1, number, 1)
    y = random.randrange(1, number, 1)
    the_task = str(x) + ' ' + str(y)
    divisible = abs(y)
    divider = abs(x)
    if abs(x) / abs(y) >= 1:
        divisible = abs(x)
        divider = abs(y)
    correct_answer = divider
    while divisible % correct_answer > 0 or divider % correct_answer > 0:
        correct_answer = correct_answer - 1
    return the_task, correct_answer

# END
