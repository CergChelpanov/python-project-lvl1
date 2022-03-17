# file <engine>

# BEGIN

import prompt

ROUNDS_COUNT = 3


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(game.RULES)
    i = ROUNDS_COUNT
    while i > 0:
        i = i - 1
        the_task, correct_answer = game.game_game()
        print('Question:', the_task)
        answer = prompt.string('Your answer: ')
        if str(answer) != str(correct_answer):
            print("'{}' is wrong answer ;(. Correct answer was'{}'.".format(
                str(answer), str(correct_answer)))
            print("Let's try again, {}!".format(name))
            exit()
        else:
            print('Correct!')
    print(f'Congratulations, {name}!')

# END
