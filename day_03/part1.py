from argparse import ArgumentParser
from pathlib import Path
import numpy as np


def build_parser():
    parser = ArgumentParser()

    parser.add_argument('input_filename', type=Path)

    return parser


def get_matches(string):
    import re

    matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', string)

    return matches


def match_to_pair(match_string):
    import re

    my_match = re.match(r'mul\((\d{1,3}),(\d{1,3})\)', match_string)

    first, second = my_match.group(1), my_match.group(2)

    return int(first), int(second)


def main():
    args = build_parser().parse_args()

    input_string = args.input_filename.read_text().strip()

    matches = get_matches(input_string)

    pairs = [
        match_to_pair(match_string)
        for match_string in matches
    ]

    products = [first * second for first, second in pairs]

    print(sum(products))


if __name__ == '__main__':
    main()
