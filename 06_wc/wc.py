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

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Main prog here """

    args = get_args()

    # print(*args.file)

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
        print(f"{num_lines:8}{num_words:8}{num_bytes:8} {fh.name}")
        fh.close()

    if len(args.file) > 1:
        print(f"{total_lines:8}{total_words:8}{total_bytes:8} total")


# --------------------------------------------------
if __name__ == '__main__':
    main()
