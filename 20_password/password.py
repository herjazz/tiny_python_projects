#!/usr/bin/env python3
"""
Title  : XKCD Password generator
Author : wrjt <wrjt@localhost>
Date   : 2021-09-14
Purpose: To generate passphrases based on dictionary words
"""

import argparse
import os
import random
import re
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Password maker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='file',
                        type=str,
                        nargs="+",
                        help='Input file(s)')

    parser.add_argument('-n',
                        '--num',
                        help='Number of passwords to generate',
                        metavar='num_passwords',
                        type=int,
                        default=3)

    parser.add_argument('-w',
                        '--num_words',
                        help='Number of words to use for password',
                        metavar='num_words',
                        type=int,
                        default=4)

    parser.add_argument('-m',
                        '--min_word_len',
                        help='Minimum word length',
                        metavar='minimum',
                        type=int,
                        default=3)

    parser.add_argument('-x',
                        '--max_word_len',
                        help='Maximum word length',
                        metavar='maximum',
                        type=int,
                        default=6)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-l',
                        '--l33t',
                        help='Obsfucate letters',
                        action='store_true')

    args = parser.parse_args()

    # Handle file not present (nargs makes it a list)
    for f in args.file:
        if not os.path.isfile(f):
            parser.error(f"No such file or directory: '{f}'")

    return args


# --------------------------------------------------
def main():
    """ Main Prog """

    args = get_args()
    random.seed(args.seed)
    words = set()
    short, long = args.min_word_len, args.max_word_len

    for f in args.file:
        with open(f, 'rt', encoding='utf-8') as fh:
            for line in fh:
                for word in map(clean, line.lower().split()):
                    if short <= len(word) <= long:
                        words.add(word.title())

    words = sorted(words)

    passwords = [
        ''.join(random.sample(words, args.num_words)) for _ in range(args.num)
    ]

    if args.l33t:
        passwords = [l33t(word) for word in passwords]

    print('\n'.join(passwords))


def clean(text: str) -> str:
    """ Clean inputted text of non-alphabet characters """
    return re.sub(re.compile(r'[^A-Za-z]'), '', text)


def ransom(text: str) -> str:
    """ Randomly CApITalIzE letters in a word """
    ransomed = [
        c.upper() if random.choice([0, 1]) else c.lower() for c in text
    ]
    return ''.join(ransomed)


def l33t(text: str) -> str:
    """ Make text l33t like """
    leet_me = {
        'a': '@',
        'A': '4',
        'O': '0',
        't': '+',
        'E': '3',
        'I': '1',
        'S': '5'
    }
    leeted = ransom(text).translate(str.maketrans(leet_me))
    return leeted + random.choice(string.punctuation)


# --------------------------------------------------
if __name__ == '__main__':
    main()
