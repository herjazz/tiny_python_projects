#!/usr/bin/env python3
"""
Author : wrjt <wrjt@localhost>
Date   : 2021-08-26
Purpose: Print a list (possibly sorted) of items to bring to a picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')


    parser.add_argument('--no_oxford',
                        help='Don\'t use an Oxford comma',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Main part of the prog """

    args = get_args()
    items = args.item
    num_items = len(items)

    if args.sorted:
        items.sort()

    if num_items == 1:
        picnic_items = items[0]
    elif num_items == 2:
        picnic_items = ' and '.join(items)
    else:
        items_except_last = ', '.join(items[:-1])
        final_item = f" and {items[-1]}" if args.no_oxford else f", and {items[-1]}"
        picnic_items = items_except_last + final_item
    print(f"You are bringing {picnic_items}.")


# --------------------------------------------------
if __name__ == '__main__':
    main()
