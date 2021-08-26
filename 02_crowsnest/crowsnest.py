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

    parser.add_argument('--starboard', default=False, action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def validate_word(supplied_word: str) -> str:
    """Check first character of supplied word is a letter"""

    if not supplied_word[0].isalpha():
        raise ValueError
    return supplied_word


# --------------------------------------------------
def main():
    """ Running with it """

    args = get_args()
    word = validate_word(args.word)
    side = 'starboard' if args.starboard else 'larboard'
    char = word[0]
    article = 'an' if char.lower() in 'aeiou' else 'a'
    if char.isupper():
        article = article.title()
    print(f"Ahoy, Captain, {article} {word} off the {side} bow!")


# --------------------------------------------------
if __name__ == '__main__':
    main()
