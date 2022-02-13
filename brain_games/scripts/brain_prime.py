#!/usr/bin/env python
# file <brain_prime>

# BEGIN

from brain_games.games import prime
from brain_games.games.mover import mover, REPEAT
import prompt
import random


def main():
    mover(prime)


if __name__ == '__main__':
    main()

# END
