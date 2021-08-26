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
                        default=False,
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Main part of the prog """

    args = get_args()
    items = args.item
    if len(items) == 1:
        picnic_items = items[0]
    else:
        if args.sorted:
            items.sort()
        items_except_last = ', '.join(items[:-1])
        final_item = f" and {items[-1]}" if len(items) == 2 else f", and {items[-1]}"
        picnic_items = items_except_last + final_item
    print(f"You are bringing {picnic_items}.")

# --------------------------------------------------
if __name__ == '__main__':
    main()
