#!/usr/bin/env python3
"""
Author : wrjt <wrjt@localhost>
Date   : 2021-08-26
Purpose: Make a python version of the command 'wc'
"""

import argparse
# import io
# import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt', encoding='utf-8'),
                        default=[sys.stdin],
                        help='Input file(s)')

    parser.add_argument('-c',
                        '--chars',
                        help='Show number of bytes',
                        action='store_true')

    parser.add_argument('-w',
                        '--words',
                        help='Show number of words',
                        action='store_true')

    parser.add_argument('-l',
                        '--lines',
                        help='Show number of lines',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def select_data(first_data: int, second_data: int, third_data: int,
                flags: str) -> None:
    """ Choose what to print, depending on flags """
    if not flags:
        return f"{first_data:8}{second_data:8}{third_data:8}"
    information = ''
    if 'l' in flags:
        information += f"{first_data:8}"
    if 'w' in flags:
        information += f"{second_data:8}"
    if 'c' in flags:
        information += f"{third_data:8}"
    return information


# --------------------------------------------------
def main():
    """ Main prog here """

    args = get_args()
    flags = ''
    if args.lines:
        flags += "l"
    if args.words:
        flags += "w"
    if args.chars:
        flags += "c"

    total_lines, total_words, total_bytes = 0, 0, 0

    for fh in args.file:
        num_lines, num_words, num_bytes = 0, 0, 0
        for line in fh:
            num_lines += 1
            num_words += len(line.split())
            num_bytes += len(line)
        total_lines += num_lines
        total_words += num_words
        total_bytes += num_bytes
        # Check for presence of flags, and print accordingly
        print(select_data(num_lines, num_words, num_bytes, flags), fh.name)
        fh.close()

    if len(args.file) > 1:
        print(
            select_data(total_lines, total_words, total_bytes, flags) +
            ' total')


# --------------------------------------------------
if __name__ == '__main__':
    main()
