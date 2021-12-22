#!/usr/bin/env python
# file brain_gcd.py

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
    print("Find the greater common divisor of given numbers.")
    x = random.randrange(1,100,1)
    y = random.randrange(1,100,1)

# Вычисление
    divisible = abs(y)
    divider = abs(x)
    if abs(x) / abs(y) >= 1:
        divisible = abs(x)
        divider = abs(y)
    
    true_result = divider
    while divisible % true_result > 0 or divider % true_result > 0:
        true_result = true_result - 1

    print("Question:",x,' ',y)
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

