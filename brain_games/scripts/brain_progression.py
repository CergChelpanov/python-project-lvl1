#!/usr/bin/env python
# file <brain_progression>

# BEGIN

from brain_games.games.progression import (
    complete_the_game, complete_the_task, what_to_do)
import prompt
import random

first_element = random.randrange(1, 50, 1)
delta = abs(random.randrange(1, 5, 1))
long_progression = 5 + random.randrange(1, 5, 1)
joker = random.randrange(1, int(long_progression), 1)
next_element = first_element
correct_answer = 2
answer = 1
wrong_answer = 2
name = ''
the_task = ''


def question(the_task, answer, correct_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    what_to_do()
    i = 3
    while i > 0:
        first_element = random.randrange(1, 50, 1)
        delta = abs(random.randrange(1, 5, 1))
        long_progression = 5 + random.randrange(1, 5, 1)
        joker = random.randrange(1, int(long_progression), 1)
        correct_answer = complete_the_game(
            first_element, delta, long_progression, joker)
        i = i - 1
        print('Question:', complete_the_task(
            first_element, delta, long_progression, joker))
        answer = prompt.string('Your answer: ')
        if str(answer) != str(correct_answer):
            wrong_answer(answer, correct_answer)
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
