# file <progression>

# BEGIN

from random import randrange, randint

RULES = 'What number is missing in the progression?'
LOWER_BOUND = 1
UPPER_BOUND_DIFF = 5
UPPER_BOUND_NUM = 10
STEP = 1


def create_progression(initial_term, number_of_elements, difference):
    return [x for x in range(initial_term,
            initial_term + number_of_elements * difference, difference)]


def go_to_string_progression(progression, indicator):
    return ' '.join([str(progression[x]) if x != indicator else '..'
                    for x in range(len(progression))])


def game_game():
    number_of_elements = 5 + randint(LOWER_BOUND, UPPER_BOUND_NUM)
    initial_term = randrange(LOWER_BOUND, number_of_elements, STEP)
    difference = abs(randrange(LOWER_BOUND, UPPER_BOUND_DIFF, STEP))
    progression = create_progression(initial_term, number_of_elements,
                                     difference)
    long_progression = 5 + randrange(LOWER_BOUND, UPPER_BOUND_DIFF, STEP)
    joker = randrange(LOWER_BOUND + 1, int(long_progression), STEP)
    miss_num = progression[joker]
    correct_answer = str(miss_num)
    the_task = go_to_string_progression(progression, joker)
    return the_task.strip(), correct_answer

# END
