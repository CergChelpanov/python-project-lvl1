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


def return_pair_question_corr_answer():
    number_of_elements = 5 + randint(LOWER_BOUND, UPPER_BOUND_NUM)
    initial_term = randrange(LOWER_BOUND, number_of_elements, STEP)
    difference = abs(randrange(LOWER_BOUND, UPPER_BOUND_DIFF, STEP))
    progression = create_progression(initial_term, number_of_elements,
                                     difference)
#    hidden_element_index = randrange(LOWER_BOUND + 1, len(progression), STEP)
# Наставник желает видеть другой вариант:
    hidden_element_index = randint(0, len(progression) - 1)
    miss_num = progression[hidden_element_index]
    correct_answer = str(miss_num)
    the_task = stringify_progression(progression, hidden_element_index)
    return the_task.strip(), correct_answer

# END
