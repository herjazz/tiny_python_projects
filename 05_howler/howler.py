#!/usr/bin/env python3
"""
Author : wrjt <wrjt@localhost>
Date   : 2021-08-26
Purpose: Return a string in UPPERCASE, either from an arg or a file and output
         to stdout or a file.
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()

    # Handle already existing file
    if os.path.isfile(args.outfile):
        parser.error(
            f'--outfile "{args.outfile}" file already exists: please choose another name.'
        )

    return args


# --------------------------------------------------
def get_file_contents(filename: str) -> str:
    """ Receive a filename and return its contents """

    with open(filename, "rt", encoding="utf-8") as infile:
        text = infile.read().rstrip()

    return text


# --------------------------------------------------
def write_message(filename: str, contents: str) -> None:
    """ Write contents of a message to a file """

    with open(filename, "wt", encoding="utf-8") as outfile:
        outfile.write(contents)


# --------------------------------------------------
def main():
    """ Main prog """

    args = get_args()
    message = args.text

    if os.path.isfile(message):
        message = get_file_contents(message)

    howled_message = message.upper()

    if args.outfile:
        write_message(args.outfile, howled_message)
    else:
        print(howled_message)


# --------------------------------------------------
if __name__ == '__main__':
    main()
