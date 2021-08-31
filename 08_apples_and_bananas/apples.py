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
                        choices=['a', 'e', 'i', 'o', 'u'],
                        default='a')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Main prog """

    args = get_args()

    vowels = 'AEIOUaeiou'

    if os.path.isfile(args.text):
        with open(args.text, 'rt', encoding='utf-8') as stream:
            args.text = stream.read()

    changed_text = ''

    for letter in args.text:
        if letter in vowels:
            if letter.isupper():
                args.vowel = args.vowel.upper()
            letter = letter.replace(letter, args.vowel)
        changed_text += letter

    print(changed_text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
