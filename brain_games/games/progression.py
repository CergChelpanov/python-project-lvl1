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


def stringify_progression(progression, hidden_element_index):
    return ' '.join([str(progression[x]) if x != hidden_element_index else '..'
                    for x in range(len(progression))])


def game_game():
    number_of_elements = 5 + randint(LOWER_BOUND, UPPER_BOUND_NUM)
    initial_term = randrange(LOWER_BOUND, number_of_elements, STEP)
    difference = abs(randrange(LOWER_BOUND, UPPER_BOUND_DIFF, STEP))
    progression = create_progression(initial_term, number_of_elements,
                                     difference)
    joker = randrange(LOWER_BOUND + 1, len(progression), STEP)
    miss_num = progression[joker]
    correct_answer = str(miss_num)
    the_task = stringify_progression(progression, joker)
    return the_task.strip(), correct_answer

# END
