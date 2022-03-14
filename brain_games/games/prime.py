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


def complete_the_game():
    number = randrange(LOWER_BOUND, UPPER_BOUND_NUM, STEP)
    the_task = str(number)
    correct_answer = 'yes'
    if is_prime(number) is True:
        correct_answer = str('yes')
        return the_task, correct_answer
    else:
        correct_answer = 'no'
    return the_task, correct_answer

# END
