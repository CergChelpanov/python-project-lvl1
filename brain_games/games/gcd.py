# file <gcd>

# BEGIN

from random import randrange, randint

RULES = 'Find the greatest common divisor of given numbers.'
START = 1
STOP = 100
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


def complete_the_game():
    number = randint(START + 1, STOP)
    x = randrange(START, number, STEP)
    y = randrange(START, number, STEP)
    the_task = str(x) + ' ' + str(y)
    correct_answer = 1
    correct_answer = gcd(x, y)
    return the_task, correct_answer

# END
