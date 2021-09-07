#!/usr/bin/env python3
"""
Title  : Mad Libs
Author : wrjt <wrjt@localhost>
Date   : 2021-09-07
Purpose: Replace parts of speech in a string with user input
"""

import argparse
import os
import re
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

    # Find part of speech (denoted by <>), return a tuple (placeholder, part)
    part_of_speech_regex = re.compile(r'(<([^<>]+)>)')

    # Assume one line of text
    matches = re.findall(part_of_speech_regex, text)
    if not matches:
        # Spit out an error and exit if no placeholders found in text
        sys.exit(f'"{args.file}" has no placeholders.')
    # Get user inputs
    tmpl = 'Give me {} {}: '
    for placeholder, part in matches:
        article = 'an' if part[0].lower() in 'aeiou' else 'a'
        answer = inputs.pop(0) if inputs else input(tmpl.format(article, part))
        text = re.sub(placeholder, answer, text, count=1)

    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
