# file <gcd>

# BEGIN

from random import randrange, randint

RULES = 'Find the greatest common divisor of given numbers.'
LOWER_BOUND = 1
UPPER_BOUND_NUM = 100
STEP = 1


def gcd(x, y):
    divisible = abs(y)
    divider = abs(x)
    if abs(x) / abs(y) >= 1:
        divisible = abs(x)
        divider = abs(y)
    correct_answer = divider
    while divisible % correct_answer > 0 or divider % correct_answer > 0:
        correct_answer = correct_answer - 1
    return correct_answer


def game_game():
    number = randint(LOWER_BOUND + 1, UPPER_BOUND_NUM)
    x = randrange(LOWER_BOUND, number, STEP)
    y = randrange(LOWER_BOUND, number, STEP)
    the_task = str(x) + ' ' + str(y)
    correct_answer = gcd(x, y)
    return the_task, correct_answer

# END
