#!/usr/bin/env python
# file brain_progression.py

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
    print("What number is missing in the progression?")
    first_element = random.randrange(1,50,1)
    delta = abs(random.randrange(1,5,1))
    long_progression = 5 + random.randrange(1,5,1)
    joker = random.randrange(1,int(long_progression),1)

# Вычисление элементов арифметической прогрессии
    next_element = first_element
    next_step = 1
    output_progression = str()
    while next_step <= long_progression:
        if next_step == joker:
            true_result = next_element
            output_progression = output_progression + ', ..'
        else:
            output_progression = output_progression + ', ' + str(next_element)
        next_element = next_element + delta
        next_step = next_step + 1
    print('Question:',output_progression)
    result_player = input('Your answer:')

#Результаты
    if int(true_result) - int(result_player) == 0:
        iteration = iteration + 1
        print('Correct!')
        if iteration == max_limit + 1:
            print("Congratulations,",name_player,"!")
    else:
        iteration = max_limit + 1
        print("'",result_player,"' is wrong answer. Correct answer was '", true_result,"'\nLet's try again,",name_player,"!")

def main():

    if __name__ == '__main__':
        main()

# END

