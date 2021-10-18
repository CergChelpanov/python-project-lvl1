# BEGIN

import random
import prompt


def welcome_user():
    name = prompt.string('May I have your name?')
    print('Hello, ', name, '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return name


def even_odd(number):
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'


def check_answer(name):
    i = 3
    while i > 0:
        i = i - 1
        question = random.randint(1, 1000)
        print('Question: ', question)
        answer = prompt.string('Your answer: ')
        if (even_odd(question) == 'even' and answer == 'yes') or (even_odd(question) == 'odd' and answer == 'no'):
            print('Correct!')
        else:
            if even_odd(question) == 'even':
                print("'", answer, "'", " is wrong answer ;(. Correct answer was 'yes'.")
                break
            else:
                print("'", answer, "'", " is wrong answer ;(. Correct answer was 'no'.")
                break
    else:
        print('Congratulations, ', name)
# END
