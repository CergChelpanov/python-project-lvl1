# file <prime>

# BEGIN

from random import randrange

RULES = 'Answer "yes" if given number is prime. Otherwise "no".'
LOWER_BOUND = 3
UPPER_BOUND_NUM = 100
STEP = 1


def is_prime(number):
    divider = 2
    if number < 2:
        return False
    while divider <= number / 2:
        if number % divider == 0:
            return False
        divider = divider + 1
    return True


def return_pair_question_corr_answer():
    number = randrange(LOWER_BOUND, UPPER_BOUND_NUM, STEP)
    the_task = str(number)
    if is_prime(number):
        correct_answer = str('yes')
    else:
        correct_answer = 'no'
    return the_task, correct_answer

# END
