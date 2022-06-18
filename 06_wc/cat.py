#!/usr/bin/env python3
"""
Title  : Cat emulation
Author : wrjt <wrjt@localhost>
Date   : 2021-08-26
Purpose: Make a python version of the command 'cat'
"""

import argparse
import io
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate the cat command',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input',
                        metavar='str',
                        nargs='*',
                        type=str,
                        default=[],
                        help='Input file(s)')

    #     parser.add_argument('-c',
    #                         '--chars',
    #                         help='Show number of bytes',
    #                         action='store_true')

    #     parser.add_argument('-w',
    #                         '--words',
    #                         help='Show number of words',
    #                         action='store_true')

    #     parser.add_argument('-l',
    #                         '--lines',
    #                         help='Show number of lines',
    #                         action='store_true')

    return parser.parse_args()


# --------------------------------------------------
# def select_data(first_data: int, second_data: int, third_data: int,
#                 flags: str) -> None:
#     """ Choose what to print, depending on flags """
#     if not flags:
#         return f"{first_data:8}{second_data:8}{third_data:8}"
#     information = ''
#     if 'l' in flags:
#         information += f"{first_data:8}"
#     if 'w' in flags:
#         information += f"{second_data:8}"
#     if 'c' in flags:
#         information += f"{third_data:8}"
#     return information


# --------------------------------------------------
def main() -> None:
    """ Main prog here """

    args = get_args()

    # print(args.input)

    for entry in args.input:
        # Check if input is a stream of text (rather than a file)
        if entry in (None, '-'):
            print(sys.stdin.readline().strip())
        elif os.path.isfile(entry):
            with open(entry, "rt", encoding="utf-8") as fh:
                print(fh.read())
        else:
            print("Unknown input")


# --------------------------------------------------
if __name__ == '__main__':
    main()
