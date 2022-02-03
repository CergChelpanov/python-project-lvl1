# file <even.py>

# BEGIN

import random

number = int(abs(random.randint(1, 1000)))
the_task = 'no worked'
correct_answer = 'not moved'


def what_to_do():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def complete_the_task(number):
    the_task = str(number)
    return the_task


def complete_the_game(number):
    if int(number) % 2 == 0:
        correct_answer = 'yes'
        return correct_answer
    else:
        correct_answer = 'no'
        return correct_answer


def main():
    complete_the_game(number)
    complete_the_task(number)
    print(complete_the_task(number), complete_the_game(number))


if __name__ == '__main__':
    main()

# END
