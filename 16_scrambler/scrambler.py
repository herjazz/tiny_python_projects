#!/usr/bin/env python3
"""
Title  : Scrambler
Author : wrjt <wrjt@localhost>
Date   : 2021-09-06
Purpose: Scrambles the middle letters in words
"""

import argparse
import os
import random
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Scramble the letters or words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()

    # Handle if text is a filename
    if os.path.isfile(args.text):
        with open(args.text, "rt", encoding="utf-8") as f:
            args.text = f.read().rstrip()

    return args


# --------------------------------------------------
def main():
    """ Main prog """

    args = get_args()
    random.seed(args.seed)

    # Regex to capture words with apostrophes (e.g. "don't")
    splitter = re.compile(
        r"""
            ([a-zA-Z]           # Capture any letter
            (?:[a-zA-Z']*       # Account for any letter plus apostrophe
            [a-zA-Z])?)         # Followed by any letter (optional group)
            """, re.VERBOSE)

    for line in args.text.splitlines():
        print(''.join([scramble(word) for word in splitter.split(line)]))


def scramble(word: str) -> str:
    """ For words longer than 3 chars, scramble middle letters """

    if len(word) > 3 and re.match(r'\w+', word):
        middle = list(word[1:-1])
        random.shuffle(middle)
        word = word[0] + ''.join(middle) + word[-1]

    return word


def test_scramble():
    """ Test scramble() """
    state = random.getstate()
    random.seed(1)
    assert scramble("a") == "a"
    assert scramble("ab") == "ab"
    assert scramble("abc") == "abc"
    assert scramble("abcd") == "acbd"
    assert scramble("abcde") == "acbde"
    assert scramble("abcdef") == "aecbdf"
    assert scramble("abcde'f") == "abcd'ef"
    random.setstate(state)


# --------------------------------------------------
if __name__ == '__main__':
    main()
