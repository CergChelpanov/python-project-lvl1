#!/usr/bin/env python
# file <brain_even>

# BEGIN

from brain_games.games import even
from brain_games.games.mover import mover, REPEAT
import prompt
import random


def main():
    mover(even)


if __name__ == '__main__':
    main()

# END
