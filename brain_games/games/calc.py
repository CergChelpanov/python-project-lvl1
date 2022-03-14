# file <calc>

# BEGIN

from random import randint, randrange

RULES = 'What is the result of the expression?'
LOWER_BOUND = 1
UPPER_BOUND_ARIPH = 4
UPPER_BOUND_NUM = 100
STEP = 1


def complete_the_game():
    number = randint(LOWER_BOUND + 1, UPPER_BOUND_NUM)
    x = randrange(LOWER_BOUND, number, STEP)
    y = randrange(LOWER_BOUND, number, STEP)
# ariphmetic - эта переменная с помощью генератора случайных чисел принимает одно из трёх значений: 1, 2, 3 каждое из которых соответсвенно выбирает в задании калькулятора один из арифметических операторв: +, -, *.
    ariphmetic = randrange(LOWER_BOUND, UPPER_BOUND_ARIPH, STEP)
    if ariphmetic == 1:
        the_task = str(x) + ' + ' + str(y)
        correct_answer = str(x + y)
        return the_task, correct_answer
    if ariphmetic == 2:
        the_task = str(x) + ' - ' + str(y)
        correct_answer = str(x - y)
        return the_task, correct_answer
    if ariphmetic == 3:
        the_task = str(x) + ' * ' + str(y)
        correct_answer = str(x * y)
        return the_task, correct_answer

# END
