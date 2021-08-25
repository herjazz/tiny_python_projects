#!/usr/bin/env python3
"""
Author : wrjt <wrjt@localhost>
Date   : 2021-08-25
Purpose: Print a sentence with a word taken from command line
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='word', help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Running with it """

    args = get_args()
    word = args.word
    char = word[0].lower()
    article = 'an' if char in 'aeiou' else 'a'
    print(f"Ahoy, Captain, {article} {word} off the larboard bow!")


# --------------------------------------------------
if __name__ == '__main__':
    main()
