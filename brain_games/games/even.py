#!/usr/bin/env python
# file <even>

# BEGIN

WHAT_TO_GO = 'Answer "yes" if the number is even, otherwise answer "no".'


def complete_the_game(number):
    the_task = str(number)
    if int(number) % 2 == 0:
        correct_answer = 'yes'
        return the_task, correct_answer
    else:
        correct_answer = 'no'
        return the_task, correct_answer

# END
