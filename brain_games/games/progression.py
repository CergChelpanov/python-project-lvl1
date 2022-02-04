# file <progression>

# BEGIN

import random

first_element = random.randrange(1, 50, 1)
delta = abs(random.randrange(1, 5, 1))
long_progression = 5 + random.randrange(1, 5, 1)
joker = random.randrange(1, int(long_progression), 1)
next_element = first_element
the_task = 'no worked'
correct_answer = 'not moved'


def what_to_do():
    print('What number is missing in the progression?')


def complete_the_task(first_element, delta, long_progression, joker):
    next_element = first_element
    next_step = 1
    the_task = ''
    while next_step <= long_progression:
        if next_step == joker:
            the_task = the_task + ' ..'
        else:
            the_task = the_task + ' ' + str(next_element)
        next_element = next_element + delta
        next_step = next_step + 1
    return the_task.strip()


def complete_the_game(first_element, delta, long_progression, joker):
    next_element = first_element
    next_step = 1
    while next_step <= long_progression:
        next_element = next_element + delta
        if next_step == joker:
            correct_answer = next_element - delta
        next_step = next_step + 1
    return correct_answer


def main():
    complete_the_game(first_element, delta, long_progression, joker)
    complete_the_task(first_element, delta, long_progression, joker)
    print(complete_the_task(
        first_element, delta, long_progression, joker), '=>', complete_the_game(
            first_element, delta, long_progression, joker))


if __name__ == '__main__':
    main()

# END
