# file <even>

# BEGIN

from random import randint
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
LOWER_BOUND = 1
UPPER_BOUND_NUM = 100


def is_even(number):
    return number % 2 == 0


def game_game():
    number = randint(LOWER_BOUND, UPPER_BOUND_NUM)
    the_task = str(number)
    if is_even(number) is True:
        correct_answer = 'yes'
        return the_task, correct_answer
    else:
        correct_answer = 'no'
        return the_task, correct_answer

# END
