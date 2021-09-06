#!/usr/bin/env python3
"""
Title  : Kentucky Friar Accent
Author : wrjt <wrjt@localhost>
Date   : 2021-09-05
Purpose: Rock the Casbah
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Southern fry text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file')

    args = parser.parse_args()

    # Handle if text is a filename
    if os.path.isfile(args.text):
        with open(args.text, "rt", encoding="utf-8") as f:
            args.text = f.read().rstrip()

    return args


# --------------------------------------------------
def main():
    """ Main Prog """

    args = get_args()

    # Saves a compile every loop and is more readable
    splitter = re.compile(r'(\W+)')
    for line in args.text.splitlines():
        words = [fry(word) for word in re.split(splitter, line.rstrip())]
        print(''.join(words))


def fry(word: str) -> str:
    """ 'Fry' a word """

    # re.match starts at the beginning of supplied string
    you_match = re.match(r'([yY])ou$', word)
    # re.search looks anywhere in the supplied string
    ing_match = re.search(r'(.+)ing$', word)
    if you_match:
        return you_match.group(1) + "'all"
    elif ing_match:
        # Check for vowels before 'ing', if present 'fry' it
        prefix = ing_match.group(1)
        if re.search(r'[aeoiuy]', prefix, re.IGNORECASE):
            return prefix + "in'"

    # # Non-regex version (passes all unit tests)
    # if word.lower() == "you":
    #     return word[0] + "'all"
    # elif word.lower().endswith('ing'):
    # # Can replace for loop with:
    # # if any(map(lambda c: c.lower() in 'aeiouy', word[:-3])):
    # #        return word[:-1] + "'"
    #     for c in word[:-3]:
    #         if c.lower() in 'aeiouy':
    #             return word[:-1] + "'"

    # Return word if not 'you' or ending in 'ing' (or one syllable 'ing')
    return word


def test_fry():
    """ Test fry() """
    assert fry('you') == "y'all"
    assert fry('You') == "Y'all"
    assert fry('your') == "your"
    assert fry('fishing') == "fishin'"
    assert fry('Aching') == "Achin'"
    assert fry('swing') == "swing"
    assert fry('trying') == "tryin'"
    assert fry('and') == "and"


# --------------------------------------------------
if __name__ == '__main__':
    main()
