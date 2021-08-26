#!/usr/bin/env python3
"""
Author : wrjt <wrjt@localhost>
Date   : 2021-08-26
Purpose: Return a string in UPPERCASE, either from an arg or a file and output
         to stdout or a file.
"""

import argparse
import io
import os
import sys


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

    if os.path.isfile(args.text):
        # QUERY: Don't we need to close this file?
        args.text = open(args.text, 'r', encoding='utf-8')
    else:
        # using io when unsure if arg is filename or string
        # (using \n to look like lines of output from a file
        args.text = io.StringIO(args.text + '\n')

    return args


# --------------------------------------------------
def main():
    """ Main prog """

    args = get_args()
    out_fh = open(args.outfile, 'wt',
                  encoding='utf-8') if args.outfile else sys.stdout
    for line in args.text:
        out_fh.write(line.upper())
    out_fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
