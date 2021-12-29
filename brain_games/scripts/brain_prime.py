#!/usr/bin/env python
# file brain_prime.py

# BEGIN

import random

# Приветствие
print("Welcome to the Brain Games!")
name_player = input('May I have your name?')
print("Hello,",name_player,"!")

# Повторы заданий

iteration = 1
max_limit = 3
while iteration <= max_limit:

# Начальные условия
    print('Answer "yes" if given number is prime. Otherwise "no".')
    given_number = abs(random.randrange(3,100,1))

# Определение простое число или нет
    divider = 2
    next_step = 1
    true_result = str('yes')

    if given_number % divider == 0:
        true_result = str('no')

    elif divider < given_number:
        divider = divider + next_step

    
    print('Question:',given_number)
    result_player = input('Your answer:')

#Результаты
    if str(true_result) == str(result_player):
        iteration = iteration + 1
        print('Correct!')
        if iteration == max_limit + 1:
            print("Congratulations,",name_player,"!")
    else:
        iteration = max_limit + 1
        print("'",str(result_player),"' is wrong answer. Correct answer was '", str(true_result),"'\nLet's try again,",name_player,"!")

def main():

    if __name__ == '__main__':
        main()
# END
