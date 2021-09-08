#!/usr/bin/env python3
"""
Title  : Mad Libs
Author : wrjt <wrjt@localhost>
Date   : 2021-09-07
Purpose: Replace parts of speech in a string with user input
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mad Libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file', metavar='file', help='Input file')

    parser.add_argument('-i',
                        '--inputs',
                        help='Inputs (for testing)',
                        metavar='input',
                        type=str,
                        default='None',
                        nargs='*')

    args = parser.parse_args()

    # Handle file not present
    if not os.path.isfile(args.file):
        parser.error(f"No such file or directory: '{args.file}'")

    return args


# --------------------------------------------------
def main():
    """ Main Prog """

    args = get_args()
    inputs = args.inputs
    with open(args.file, 'rt', encoding='utf-8') as f:
        text = f.read().rstrip()

    if find_brackets(text) is None:
        # Spit out an error and exit if no placeholders found in text
        sys.exit(f'"{args.file}" has no placeholders.')

    # Get user inputs
    nu_text = ''
    tmpl = 'Give me {} {}: '

    while find_brackets(text) is not None:
        left, right = find_brackets(text)
        article = 'an' if text[left + 1].lower() in 'aeiou' else 'a'
        if inputs:
            word = inputs.pop(0)
        else:
            word = input(tmpl.format(article, text[left + 1:right]))
        nu_text += text[:left] + word
        text = text[right + 1:]

    text = nu_text + text
    print(text)


def find_brackets(text: str) -> tuple:
    """
    Find position of angled brackets in a string and return as a tuple (start, end)

    ISSUES:
        - Will return a value for "<adjective noun>" which isn't what we want
          (Maybe can resolve this by checking returned str matches certain
          values - done outside of this function though)
        - Will let mismatched brackets through (e.g. "<<hello>")
          (again, resolvable outside of function)
    """
    start, end = text.find('<'), text.find('>')
    gap = end - start
    # str.find will return -1 if substr not found
    if any([gap == 1, start == -1, end == -1]):
        return None
    return (start, end)


def test_find_brackets():
    """ Test find_brackets() """
    assert find_brackets('') is None
    assert find_brackets('<>') is None
    assert find_brackets('<x>') == (0, 2)
    assert find_brackets('foo <bar> baz') == (4, 8)
    assert find_brackets('foo bar> baz') is None
    assert find_brackets('foo <bar baz') is None
    # Below will fail but tedious to implement inside function
    # Better to deal with it by checking str outside of function
    # assert find_brackets('foo <<bar> baz') == None


# --------------------------------------------------
if __name__ == '__main__':
    main()
