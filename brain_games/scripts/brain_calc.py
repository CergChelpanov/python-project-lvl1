#!/usr/bin/env python
# file <brain_calc>

# BEGIN

from brain_games.games import calc
from brain_games.games.mover import mover, REPEAT
import prompt
import random


def main():
    mover(calc)


if __name__ == '__main__':
    main()
# END
