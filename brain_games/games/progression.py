# file <progression>

# BEGIN

from random import randrange, randint

RULES = 'What number is missing in the progression?'
LOWER_BOUND = 1
UPPER_BOUND_DELTA = 5
UPPER_BOUND_NUM = 10
STEP = 1


def create_progression(first_num, number_of_elements, delta):
    return [x for x in range(first_num,
            first_num + number_of_elements * delta, delta)]


def go_to_string_progression(progression, indicator):
    return ' '.join([str(progression[x]) if x != indicator else '..'
                    for x in range(len(progression))])


def complete_the_game():
    number_of_elements = 5 + randint(LOWER_BOUND, UPPER_BOUND_NUM)
    first_num = randrange(LOWER_BOUND, number_of_elements, STEP)
    delta = abs(randrange(LOWER_BOUND, UPPER_BOUND_DELTA, STEP))
    progression = create_progression(first_num, number_of_elements, delta)
    long_progression = 5 + randrange(LOWER_BOUND, UPPER_BOUND_DELTA, STEP)
    joker = randrange(LOWER_BOUND + 1, int(long_progression), STEP)
    miss_num = progression[joker]
    correct_answer = str(miss_num)
    the_task = go_to_string_progression(progression, joker)
    return the_task.strip(), correct_answer

# END
