#!/usr/bin/env python
# file <brain_prime>

# BEGIN

from brain_games.games.prime import (
    complete_the_game, complete_the_task, what_to_do)
import prompt
import random

correct_answer = 2
answer = 1
wrong_answer = 2
name = ''
the_task = ''
number = int(abs(random.randrange(3, 100, 1)))


def question(the_task, answer, correct_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    what_to_do()
    i = 3
    while i > 0:
        number = int(abs(random.randrange(3, 100, 1)))
        correct_answer = complete_the_game(number)
        i = i - 1
        print('Question:', complete_the_task(number))
        answer = prompt.string('Your answer: ')
        if str(answer) != str(correct_answer):
            wrong_answer(answer, correct_answer)
            print("Let's try again, {}!".format(name))
            quit()
        else:
            true_answer()
    print(f'Congratulations, {name}!')


def wrong_answer(wrong_answer, correct_answer):
    print("'{}' is wrong answer ;(. Correct answer was'{}'.".format(
        wrong_answer, correct_answer))


def true_answer():
    print('Correct!')


def main():
    question(the_task, answer, correct_answer)


if __name__ == '__main__':
    main()

# END
