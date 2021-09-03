#!/usr/bin/env python3
"""
Author : wrjt <wrjt@localhost>
Date   : 2021-09-03
Purpose: To generate "bottle of beer" song dpeneding on the value of n
(default: 10)
"""

import argparse
# import textwrap as tw


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='number',
                        type=int,
                        default=10)

    args = parser.parse_args()

    # Handle out of bounds error for number of bottles
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
# def verse(bottle: int) -> str:
#     """ Sing a verse """
#     if bottle == 2:
#         verse = tw.dedent("""\
#         2 bottles of beer on the wall,
#         2 bottles of beer,
#         Take one down, pass it around,
#         1 bottle of beer on the wall!
#         """)
#     elif bottle == 1:
#         verse = tw.dedent("""\
#         1 bottle of beer on the wall,
#         1 bottle of beer,
#         Take one down, pass it around,
#         No more bottles of beer on the wall!""")
#     else:
#         verse = tw.dedent(f"""\
#         {bottle} bottles of beer on the wall,
#         {bottle} bottles of beer,
#         Take one down, pass it around,
#         {bottle - 1} bottles of beer on the wall!
#         """)

#     return verse


def verse(bottle):
    """ Sing a verse """

    current_bottle = '1 bottle' if bottle == 1 else f'{bottle} bottles'
    next_bottle = 'No more bottles' if bottle == 1 else f'{bottle - 1} bottle' if bottle == 2 else f'{bottle - 1} bottles'

    return '\n'.join([
        f'{current_bottle} of beer on the wall,', f'{current_bottle} of beer,',
        'Take one down, pass it around,', f'{next_bottle} of beer on the wall!'
    ])


# --------------------------------------------------
def main():
    """ Main Prog """

    args = get_args()

    # for i in range(args.num, 0, -1):
    #     print(verse(i))

    print('\n\n'.join(map(verse, range(args.num, 0, -1))))


def test_verse():
    """ Test verse """

    last_verse = verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])

    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,', '1 bottle of beer on the wall!'
    ])


# --------------------------------------------------
if __name__ == '__main__':
    main()
