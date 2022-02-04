# file <prime>

# BEGIN


import random

number = int(abs(random.randrange(3, 100, 1)))
the_task = 'no worked'
correct_answer = 'yes'


def what_to_do():
    print('Answer "yes" if given number is prime. Otherwise "no".')


def complete_the_task(number):
    the_task = str(number)
    return the_task


def complete_the_game(number):
    divider = 2
    correct_answer = 'yes'
    while divider <= (number / 2):
        if number % divider == 0:
            correct_answer = str('no')
            return correct_answer
        elif divider < number:
            divider = divider + 1
    return correct_answer


def main():
    complete_the_game(number)
    complete_the_task(number)
    print(complete_the_task(number), complete_the_game(number))


if __name__ == '__main__':
    main()

# END
