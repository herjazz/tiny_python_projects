#!/usr/bin/env python3
"""
Author : wrjt <wrjt@localhost>
Date   : 2021-08-26
Purpose: Use 'jump-the-five' encoding to unscramble phone numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main prog"""

    args = get_args()
    encoded_text = args.text

    jump_dict = {
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "5": "0",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
        "0": "5"
    }

    decoded_text = ''

    for char in encoded_text:
        decoded_text += jump_dict.get(char, char)

    print(decoded_text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
