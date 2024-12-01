from argparse import ArgumentParser
from collections import Counter
from pathlib import Path


def build_parser():
    parser = ArgumentParser()

    parser.add_argument('input_filename', type=Path)

    return parser


def main():
    args = build_parser().parse_args()

    lines = args.input_filename.read_text().splitlines()
    pairs = [list(map(int, line.split())) for line in lines]
    list1, list2 = map(lambda x: list(sorted(x)), zip(*pairs))
    counts = Counter(list2)
    similarity = [element * counts[element] for element in list1]
    print(sum(similarity))


if __name__ == '__main__':
    main()
