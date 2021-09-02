#!/usr/bin/env python3
"""
Author : wrjt <wrjt@localhost>
Date   : 2021-09-02
Purpose: A game of telephone that randomly mutates text
"""

import argparse
import os
import random
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
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

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    args = parser.parse_args()

    # Handle out of bounds error for mutations
    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    # Handle if text is a filename
    if os.path.isfile(args.text):
        with open(args.text, "rt", encoding="utf-8") as f:
            args.text = f.read().rstrip()

    return args


# --------------------------------------------------
def main():
    """ Main prog """

    args = get_args()
    text = args.text
    random.seed(args.seed)
    num_mutations = round(len(text) * args.mutations)

    # Get all letters and punctuation for mutation
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))

    # Choose indices to change in text
    indexes = random.sample(range(len(text)), num_mutations)

    new_text = ''
    # Below works, but has different results from book version - why?
    for idx, char in enumerate(text):
        if idx in indexes:
            # Remove char from alpha so it cannot be put back into new string
            new_text += random.choice(alpha.replace(char, ''))
        else:
            new_text += char

    # BOOK ANSWER
    # does the process far quicker than my one (10 times!)
    # new_text = text
    # for i in indexes:
    #     new_char = random.choice(alpha.replace(new_text[i], ''))
    #     new_text = new_text[:i] + new_char + new_text[i + 1:]

    # Extra space before 2nd ':' to line up with first one.
    print(f'You said: "{text}"\nI heard : "{new_text}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
