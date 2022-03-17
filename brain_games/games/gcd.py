# file <gcd>

# BEGIN

from random import randrange, randint

RULES = 'Find the greatest common divisor of given numbers.'
LOWER_BOUND = 1
UPPER_BOUND_NUM = 100
STEP = 1


def gcd(x, y):
    #    divisible = abs(y)
    #    divider = abs(x)
    #    if abs(x) / abs(y) >= 1:
    #        divisible = abs(x)
    #        divider = abs(y)
    #    correct_answer = divider
    #    while divisible % correct_answer > 0 or divider % correct_answer > 0:
    #        correct_answer = correct_answer - 1
    # Наставник желает видеть решение алгоритмом Евклида:
    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    correct_answer = x + y
    return correct_answer


def return_pair_question_corr_answer():
    number = randint(LOWER_BOUND + 1, UPPER_BOUND_NUM)
    x = randrange(LOWER_BOUND, number, STEP)
    y = randrange(LOWER_BOUND, number, STEP)
    the_task = str(x) + ' ' + str(y)
    correct_answer = gcd(x, y)
    return the_task, correct_answer

# END
