#!/usr/bin/env python
# file <prime>

# BEGIN

import random

WHAT_TO_GO = 'Answer "yes" if given number is prime. Otherwise "no".'


def complete_the_game(number):
    number = int(abs(random.randrange(3, 100, 1)))
    the_task = str(number)
    divider = 2
    correct_answer = 'yes'
    while divider <= (number / 2):
        if number % divider == 0:
            correct_answer = str('no')
            return the_task, correct_answer
        elif divider < number:
            divider = divider + 1
    return the_task, correct_answer

# END
