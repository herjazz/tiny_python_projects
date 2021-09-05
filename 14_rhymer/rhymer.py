#!/usr/bin/env python3
"""
Title  : Rhymer
Author : wrjt <wrjt@localhost>
Date   : 2021-09-04
Purpose: Find rhyming words using regexes
"""

import argparse
import re
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='word', help='A word to rhyme')

    args = parser.parse_args()

    # if len(args.word) != 1:
    #     parser.error("Please only enter one word.")

    return args


# --------------------------------------------------
def main():
    """ Main prog """

    args = get_args()

    consonants = list('bcdfghjklmnpqrstvwxyz')
    clusters = """\
            bl br ch cl cr dr fl fr gl gr pl pr sc sh sk sl sm sn sp st sw th
            tr tw thw wh wr sch scr shr sph spl spr squ str thr""".split()
    prefixes = sorted(consonants + clusters)

    remove_me, stem = stemmer(args.word)

    if stem:
        output = '\n'.join([p + stem for p in prefixes if p != remove_me])
    else:
        output = f'Cannot rhyme "{args.word}"'

    print(output)


def stemmer(word: str) -> tuple:
    """ Return leading consonants (if any), and 'stem' of the word """

    letters, vowels = string.ascii_lowercase, 'aeiou'
    consonants = ''.join([c for c in letters if c not in vowels])
    word = word.lower()

    # Alternative using re.compile and findall (which returns a list)
    pattern_regex = re.compile(
        rf'''(
            ([{consonants}]+)?          # Capture one or more (optional)
            ([{vowels}]+)               # Capture at least one vowel
            (.*)                        # Capture zero or more of anything else
            )''', re.VERBOSE)

    match = pattern_regex.findall(word)

    if match:
        p1 = match[0][1] or ''
        p2 = match[0][2] or ''
        p3 = match[0][3] or ''
        return (p1, p2 + p3)
    else:
        return (word, '')

    # pattern = f'([{consonants}]+)?([{vowels}])(.*)'
    # match = re.match(pattern, word)

    # if match:
    #     p1 = match.group(1) or ''
    #     p2 = match.group(2) or ''
    #     p3 = match.group(3) or ''
    #     return (p1, p2 + p3)
    # else:
    #     return (word, '')


def test_stemmer():
    """ Test stemmer() """
    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDNZL') == ('rdnzl', '')
    assert stemmer('123') == ('123', '')


# --------------------------------------------------
if __name__ == '__main__':
    main()
