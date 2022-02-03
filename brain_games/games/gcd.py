# file <gcd>

# BEGIN

import random

x = random.randrange(1, 100, 1)
y = random.randrange(1, 100, 1)
the_task = 'no worked'
correct_answer = 'not moved'


def what_to_do():
    print('Find the greatest common divisor of given numbers.')


def complete_the_task(x, y):
    the_task = str(x) + ' ' + str(y)
    return the_task


def complete_the_game(x, y):
    divisible = abs(y)
    divider = abs(x)
    if abs(x) / abs(y) >= 1:
        divisible = abs(x)
        divider = abs(y)
    correct_answer = divider
    while divisible % correct_answer > 0 or divider % correct_answer > 0:
        correct_answer = correct_answer - 1
    return correct_answer


def main():
    complete_the_game(x, y)
    complete_the_task(x, y)
    print(complete_the_task(x, y), '=>', complete_the_game(x, y))


if __name__ == '__main__':
    main()
# END
