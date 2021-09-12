#!/usr/bin/env python3
"""
Title  : Workout of the Day
Author : wrjt <wrjt@localhost>
Date   : 2021-09-10
Purpose: Create a random daily workout from choices in a csv file
"""

import argparse
import csv
import io
import os
import random
import re
import sys

from tabulate import tabulate


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create Workout Of (the) Day (WOD)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='CSV input file of exercises',
                        metavar='FILE',
                        type=str,
                        default='./inputs/exercises.csv')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        help='Number of exercises',
                        metavar='exercises',
                        type=int,
                        default=4)

    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps',
                        action='store_true')

    args = parser.parse_args()

    # Handle out of bounds error for number of exercises
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    # Handle empty file
    if os.path.getsize(args.file) == 0:
        parser.error(f"File: '{args.file}' appears to be empty")

    # Handle file not present
    if not os.path.isfile(args.file):
        parser.error(f"No such file or directory: '{args.file}'")

    return args


# --------------------------------------------------
def main():
    """ Main prog """

    args = get_args()
    random.seed(args.seed)
    with open(args.file, 'rt', encoding='utf-8') as f:
        exercises = read_csv(f)

    # Deal with any badly formed data (read_csv returns None)
    if not exercises:
        sys.exit(f'No usable data in --file "{args.file}"')

    # Check if trying to sample more exercises than are actually in the file
    num_exercises = len(exercises)
    if args.num > num_exercises:
        sys.exit(f'--num "{args.num}" > exercises "{num_exercises}"')

    wod = []
    for name, low, high in random.sample(exercises, k=args.num):
        suggested_reps = random.randint(low, high)
        if args.easy:
            # Round down any fractional results
            suggested_reps = suggested_reps // 2
        wod.append((name, suggested_reps))

    print(tabulate(wod, headers=('Exercise', 'Reps')))


def read_csv(fh) -> list:
    """ Read CSV formatted input, returns a list of tuples """
    reader = csv.reader(fh)
    # Skip past headers
    _ = next(reader)
    exercises = []
    for row in reader:
        name, reps = row
        # Check each record has both items
        if name and reps:
            # Check data is as expected for reps (eg. number-number)
            match = re.match(r'(\d+)-(\d+)', reps)
            if match:
                low, high = [int(value) for value in reps.split('-')]
                exercises.append((name, low, high))
    return exercises

# Removed unit test to separate file.

# --------------------------------------------------
if __name__ == '__main__':
    main()
