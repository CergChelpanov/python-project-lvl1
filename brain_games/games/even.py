# file <even>

# BEGIN

from random import randint
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
LOWER_BOUND = 1
UPPER_BOUND_NUM = 100


def is_even(number):
    return number % 2 == 0


def return_pair_question_corr_answer():
    number = randint(LOWER_BOUND, UPPER_BOUND_NUM)
    the_task = str(number)
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return the_task, correct_answer

# END
