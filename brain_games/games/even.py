# file <even>

# BEGIN

from random import randint
RULES_OF_THE_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'
START = 1
STOP = 100


def complete_the_game():
    number = randint(START, STOP)
    the_task = str(number)

    def is_even(number):
        return number % 2 == 0
    if is_even(number) is True:
        correct_answer = 'yes'
        return the_task, correct_answer
    else:
        correct_answer = 'no'
        return the_task, correct_answer

# END
