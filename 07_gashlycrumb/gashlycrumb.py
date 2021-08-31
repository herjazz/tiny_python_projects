#!/usr/bin/env python3
"""
Author : wrjt <wrjt@localhost>
Date   : 2021-08-30
Purpose: Extract a line of text from Gashlycrumb that matches letter(s)
supplied on command line. Takes an optional argument to use a different source
file.
"""

import argparse
import os
# import sys
# import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        nargs='+',
                        help='Letter(s)')

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=str,
                        default='./gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Main program """

    args = get_args()
    letter_choices = args.letter

    # Extract text line-by-line from file
    try:
        with open(args.file, 'r', encoding='utf-8') as src_file:
            text = src_file.readlines()
            # text = [line.rstrip() for line in text]
    except FileNotFoundError:
        print("No file matches")
        # sys.exit()
    else:
        # Make dict that alphabetizes a dict extracting line for each value
        # keys = string.ascii_lowercase
        # letter_dict = {k: v for k, v in zip(keys, text)}
        letter_dict = {line[0].upper(): line.rstrip() for line in text}

        for letter in letter_choices:
            print(letter_dict.get(letter.upper(), f'I do not know "{letter}".'))


# --------------------------------------------------
if __name__ == '__main__':
    main()
