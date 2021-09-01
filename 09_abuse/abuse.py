#!/usr/bin/env python3
"""
Author : wrjt <wrjt@localhost>
Date   : 2021-09-01
Purpose: A file that fires out random insults taken from a corpus of nouns and
adjectives
"""

import argparse
import random
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Heap abuse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-a',
                        '--adjectives',
                        help='Number of adjectives',
                        metavar='adjectives',
                        type=int,
                        default=2)

    parser.add_argument('-n',
                        '--number',
                        help='Number of insults',
                        metavar='insults',
                        type=int,
                        default=1)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')

    return args


def read_file(filename: str) -> str:
    """ Read a file and return its contents in a list, raise FileNotFoundError
    if there's an issue """
    if os.path.isfile(filename):
        with open(filename, 'rt', encoding='utf-8') as f:
            return f.read().split()
    else:
        raise FileNotFoundError(f"{filename} does not exist.")


# --------------------------------------------------
def main():
    """ Main prog """

    args = get_args()
    random.seed(args.seed)

    adjectives = read_file('./adjectives.txt')

    nouns = read_file('./nouns.txt')

    for _ in range(args.number):
        # Using random.sample as the choices are unique
        chosen_adjs = ', '.join(random.sample(adjectives, args.adjectives))
        print(f"You {chosen_adjs} {random.choice(nouns)}!")


# --------------------------------------------------
if __name__ == '__main__':
    main()
