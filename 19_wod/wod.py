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

    output = []
    for ex in random.sample(exercises, k=args.num):
        suggested_reps = random.randint(ex[1], ex[2])
        if args.easy:
            suggested_reps = suggested_reps // 2
        output.append((ex[0], suggested_reps))

    print(tabulate(output, headers=('Exercise', 'Reps')))


def read_csv(fh) -> list:
    """ Read CSV formatted input, returns a list of tuples """
    reader = csv.reader(fh)
    # Skip past headers
    _ = next(reader)
    exercises = []
    for row in reader:
        name, reps = row
        low, high = [int(value) for value in reps.split('-')]
        exercises.append((name, low, high))
    return exercises


def test_read_csv():
    """ Test read_csv functions """
    # Make a fake file handle using io module
    text = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,40-100')
    assert read_csv(text) == [('Burpees', 20, 50), ('Situps', 40, 100)]


# --------------------------------------------------
if __name__ == '__main__':
    main()
