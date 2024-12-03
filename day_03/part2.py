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


def split_on_disabled_sections(input_string):
    import re

    return re.split(
        r"(don't\(\)|do\(\))", input_string
    )


def main():
    args = build_parser().parse_args()

    input_string = args.input_filename.read_text().strip()

    input_strings = split_on_disabled_sections(input_string)

    mul_enabled = True
    products = []
    for string in input_strings:
        if string == 'do()':
            mul_enabled = True
        elif string == "don't()":
            mul_enabled = False
        elif mul_enabled:
            matches = [
                my_match
                for my_match in get_matches(string)
            ]

            pairs = [
                match_to_pair(match_string)
                for match_string in matches
            ]

            products += [first * second for first, second in pairs]

    print(sum(products))


if __name__ == '__main__':
    main()
