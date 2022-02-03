#!/usr/bin/env python
# file <brain_games.py>

# BEGIN

from brain_games.cli import welcome_user


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    welcome_user()


if __name__ == '__main__':
    main()

# END

