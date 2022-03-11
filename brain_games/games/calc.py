# file <calc>

# BEGIN

from random import randint, randrange

RULES_OF_THE_GAME = 'What is the result of the expression?'
START = 1
STOP1 = 4
STOP2 = 100
STEP = 1


def complete_the_game():
    number = randint(START, STOP2)
    x = randrange(START, number, STEP)
    y = randrange(START, number, STEP)
    arifmetic = randrange(START, STOP1, STEP)
    if arifmetic == 1:
        the_task = str(x) + ' + ' + str(y)
        correct_answer = str(x + y)
        return the_task, correct_answer
    if arifmetic == 2:
        the_task = str(x) + ' - ' + str(y)
        correct_answer = str(x - y)
        return the_task, correct_answer
    if arifmetic == 3:
        the_task = str(x) + ' * ' + str(y)
        correct_answer = str(x * y)
        return the_task, correct_answer

# END
