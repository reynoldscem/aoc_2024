from argparse import ArgumentParser
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
    differences = [abs(first - second) for first, second in zip(list1, list2)]

    print(sum(differences))


if __name__ == '__main__':
    main()
