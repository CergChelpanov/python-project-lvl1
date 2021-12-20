#!/usr/bin/env python
# file brain_calc.py

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

# Задание
    print("What is the result of the expression?")
    x = random.randrange(1,100,1)
    y = random.randrange(1,100,1)
    arifmetic = random.randrange(1,4,1)
    if arifmetic == 1:
        true_result = x + y
        print("Question:",x,"+",y)
    if arifmetic == 2:
        true_result = x - y
        print("Question:",x,"-",y)
    if arifmetic == 3:
        true_result = x * y
        print("Question:",x,"*",y)
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
