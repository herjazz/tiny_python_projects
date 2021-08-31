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

    # Extract text line-by-line from file
    try:
        with open(args.file, 'r', encoding='utf-8') as src_file:
            text = src_file.readlines()
    except FileNotFoundError:
        print("No file matches")
    else:
        letter_dict = {line[0].upper(): line.rstrip() for line in text}

        while True:
            user_choice = input("Please provide a letter [! to quit]: ")

            if user_choice == "!":
                print("Bye")
                break

            print(letter_dict.get(user_choice.upper(), f'I do not know "{user_choice}".'))


# --------------------------------------------------
if __name__ == '__main__':
    main()
