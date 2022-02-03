# file <calc>

# BEGIN

import random

x = random.randrange(1, 100, 1)
y = random.randrange(1, 100, 1)
arifmetic = random.randrange(1, 4, 1)
the_task = 'no worked'
correct_answer = 'not moved'


def what_to_do():
    print('What is the result of the expression?')


def complete_the_task(x, y, arifmetic):
    if arifmetic == 1:
        the_task = str(x) + '+' + str(y)
        return the_task
    if arifmetic == 2:
        the_task = str(x) + '-' + str(y)
        return the_task
    if arifmetic == 3:
        the_task = str(x) + '*' + str(y)
        return the_task


def complete_the_game(x, y, arifmetic):
    if arifmetic == 1:
        correct_answer = str(x + y)
        return correct_answer
    if arifmetic == 2:
        correct_answer = str(x - y)
        return correct_answer
    if arifmetic == 3:
        correct_answer = str(x * y)
        return correct_answer


def main():
    complete_the_game(x, y, arifmetic)
    complete_the_task(x, y, arifmetic)
    print(complete_the_task(x, y, arifmetic), '=', complete_the_game(
        x, y, arifmetic))


if __name__ == '__main__':
    main()

# END
