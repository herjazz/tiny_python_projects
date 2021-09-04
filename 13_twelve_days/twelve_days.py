#!/usr/bin/env python3
"""
Title  : Twelve Days Of Christmas
Author : wrjt <wrjt@localhost>
Date   : 2021-09-04
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Twelve Days Of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of days to sing',
                        metavar='days',
                        type=int,
                        default=12)

    parser.add_argument('-o',
                        '--output',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()

    # Handle out of bounds error for number of days
    if args.num not in range(1, 13):
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


# --------------------------------------------------
def main():
    """ Main Prog """

    args = get_args()

    # verses = '\n\n'.join(map(verse, range(1, args.num + 1)))
    verses = '\n\n'.join([verse(n) for n in range(1, args.num + 1)])

    if args.output:
        with open(args.output, 'wt', encoding='utf-8') as outfile:
            outfile.write(verses + '\n')
    else:
        print(verses)


def verse(day: int) -> str:
    """ Return a verse of 12 Days of Xmas """

    ordinals = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth',
                'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

    gifts = ['A partridge in a pear tree.',
             'Two turtle doves,',
             'Three French hens,',
             'Four calling birds,',
             'Five gold rings,',
             'Six geese a laying,',
             'Seven swans a swimming,',
             'Eight maids a milking,',
             'Nine ladies dancing,',
             'Ten lords a leaping,',
             'Eleven pipers piping,',
             'Twelve drummers drumming,']

    lines = [f"On the {ordinals[day - 1]} day of Christmas,",
             "My true love gave to me,"]

    for gift in reversed(gifts[1:day]):
        lines.append(gift)

    if day > 1:
        lines.append("And " + gifts[0].lower())
    else:
        lines.append(gifts[0])

    # # Book version
    # lines.extend(reversed(gifts[:day]))

    # if day > 1:
        # lines[-1] = 'And '+ lines[-1].lower()

    return '\n'.join(lines)


def test_verse():
    """ Test verse() """

    assert verse(1) == '\n'.join([
        'On the first day of Christmas,', 'My true love gave to me,',
        'A partridge in a pear tree.'
    ])

    assert verse(2) == '\n'.join([
        'On the second day of Christmas,', 'My true love gave to me,',
        'Two turtle doves,', 'And a partridge in a pear tree.'
    ])

    assert verse(3) == '\n'.join([
        'On the third day of Christmas,', 'My true love gave to me,',
        'Three French hens,', 'Two turtle doves,',
        'And a partridge in a pear tree.'
    ])


# --------------------------------------------------
if __name__ == '__main__':
    main()
