#!/usr/bin/env python3
"""
Title  : Ransom Note
Author : wrjt <wrjt@localhost>
Date   : 2021-09-04
Purpose: Encode some text with random capitaization
"""

import argparse
import os
import random


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random Seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()

    # Handle if text is a filename
    if os.path.isfile(args.text):
        with open(args.text, "rt", encoding="utf-8") as f:
            args.text = f.read().rstrip()

    return args


def main():
    """ Main Prog """

    args = get_args()
    random.seed(args.seed)

    ransom_note = [choose(char) for char in args.text]
    # ransom_note = map(choose, args.text)

    print(''.join(ransom_note))


def choose(char: str) -> str:
    """ Change case of a character randomly """

    # # My version returned different results than his - why?
    # return random.choice([char.upper(), char.lower()])
    return char.upper() if random.choice([0, 1]) else char.lower()


def test_choose():
    """ Test choose() """

    state = random.getstate()
    random.seed(1)
    assert choose('a') == 'a'
    assert choose('b') == 'b'
    assert choose('c') == 'C'
    assert choose('d') == 'd'
    random.setstate(state)


# --------------------------------------------------
if __name__ == '__main__':
    main()
