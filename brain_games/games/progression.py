#!/usr/bin/env python
# file <progression>

# BEGIN

import random

WHAT_TO_GO = 'What number is missing in the progression?'


def complete_the_game(number):
    first_element = random.randrange(1, number, 1)
    delta = abs(random.randrange(1, 5, 1))
    long_progression = 5 + random.randrange(1, 5, 1)
    joker = random.randrange(1, int(long_progression), 1)
    next_element = first_element
    next_step = 1
    the_task = ''
    while next_step <= long_progression:
        if next_step == joker:
            the_task = the_task + ' ..'
        else:
            the_task = the_task + ' ' + str(next_element)
        next_element = next_element + delta
        next_step = next_step + 1
    next_element = first_element
    next_step = 1
    while next_step <= long_progression:
        next_element = next_element + delta
        if next_step == joker:
            correct_answer = next_element - delta
        next_step = next_step + 1
    return the_task.strip(), correct_answer

# END
