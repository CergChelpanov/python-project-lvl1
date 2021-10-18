#!/usr/bin/env python

# BEGIN

from brain_games.even import welcome_user
from brain_games.even import check_answer


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    check_answer(welcome_user())


if __name__ == '__main__':
    main()

# END
