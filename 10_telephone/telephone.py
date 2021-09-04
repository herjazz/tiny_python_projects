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
# import sys


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

    parser.add_argument('-o',
                        '--output',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-c',
                        '--characters',
                        help='Only use characters to replace',
                        action='store_true')

    args = parser.parse_args()

    # Handle out of bounds error for mutations
    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    # Handle if text is a filename
    if os.path.isfile(args.text):
        with open(args.text, "rt", encoding="utf-8") as f:
            args.text = f.read().rstrip()

    # Handle already existing file
    if os.path.isfile(args.output):
        parser.error(
            f'--output "{args.output}" file already exists: please choose another name.'
        )

    return args


# --------------------------------------------------
def main():
    """ Main prog """

    args = get_args()
    text = args.text
    random.seed(args.seed)
    num_mutations = round(len(text) * args.mutations)

    # Get all letters (and punctuation) for mutation
    if args.characters:
        alpha = string.ascii_letters
    else:
        alpha = ''.join(sorted(string.ascii_letters + string.punctuation))

    # Choose indices to change in text
    indexes = random.sample(range(len(text)), num_mutations)

    # new_text = ''
    # # Below works, but has different results from book version - why?
    # for idx, char in enumerate(text):
    #     if idx in indexes:
    #         # Remove char from alpha so it cannot be put back into new string
    #         new_text += random.choice(alpha.replace(char, ''))
    #     else:
    #         new_text += char

    # # # BOOK ANSWER
    # # does the process far quicker than my one (10 times!)
    # new_text = text
    # for i in indexes:
    #     # Remove char from alpha so it cannot be put back into new string
    #     new_char = random.choice(alpha.replace(new_text[i], ''))
    #     new_text = new_text[:i] + new_char + new_text[i + 1:]

    # # BOOK ANSWER - LIST APPROACH
    #
    new_text = list(text)
    for i in indexes:
        new_text[i] = random.choice(alpha.replace(new_text[i], ''))

    new_text = ''.join(new_text)

    # Extra space before 2nd ':' to line up with first one.
    message = f'You said: "{text}"\nI heard : "{new_text}"'

    if args.output:
        with open(args.output, 'wt', encoding='utf-8') as outfile:
            outfile.write(message + '\n')
    else:
        print(message)


# --------------------------------------------------
if __name__ == '__main__':
    main()
