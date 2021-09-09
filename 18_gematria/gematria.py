#!/usr/bin/env python3
"""
Title  : gematria.py
Author : wrjt <wrjt@localhost>
Date   : 2021-09-09
Purpose: numerically encode a word using values for characters
         (using ASCII values)
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gematria',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    args = parser.parse_args()

    # Handle if text is a filename
    if os.path.isfile(args.text):
        with open(args.text, "rt", encoding="utf-8") as f:
            args.text = f.read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # Book version
    # for line in args.text.splitlines():
    #     print(' '.join(map(word2num, line.split())))

    for line in args.text.splitlines():
        print(' '.join([word2num(word) for word in line.split()]))


def word2num(word: str) -> str:
    """ Convert a word to the sum of its ascii values """

    # # Book version:
    # return str(sum(map(ord, re.sub(r'[^A-Za-z0-9]', '', word))))

    # Remove non-letters and numbers
    word = re.sub(re.compile(r'[^A-Za-z0-9]'), '', word)
    return str(sum(ord(c) for c in word))


def test_word2num():
    """ Test word2num() """
    assert word2num("a") == "97"
    assert word2num("abc") == "294"
    assert word2num("ab'c") == "294"
    assert word2num("4a-b'c,") == "346"


# --------------------------------------------------
if __name__ == '__main__':
    main()
