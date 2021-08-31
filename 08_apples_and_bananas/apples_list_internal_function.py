#!/usr/bin/env python3
"""
Author : wrjt <wrjt@localhost>
Date   : 2021-08-31
Purpose: A program which substitutes vowels in text with a supplied vowel
(default: 'a')
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        choices=list('aeiou'),
                        default='a')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        with open(args.text, 'rt', encoding='utf-8') as stream:
            args.text = stream.read().rstrip()

    return args


# --------------------------------------------------
def main():
    """ Main prog """

    args = get_args()
    text = args.text
    vowel = args.vowel

    def new_char(c):
        """ Returns character depending on conditions """
        # NOTE: This funcation *can* access variables inside main()!!! (e.g. vowel)
        return vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c

    text = ''.join([new_char(letter) for letter in text])
    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
