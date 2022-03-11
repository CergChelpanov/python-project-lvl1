# file <mover>

# BEGIN

import prompt

REPEAT = 3


def mover(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(game.RULES_OF_THE_GAME)
    i = REPEAT
    while i > 0:
        i = i - 1
        the_task, correct_answer = game.complete_the_game()
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
